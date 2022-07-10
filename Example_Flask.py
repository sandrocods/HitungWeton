import base64
import warnings
from src.HitungWeton import *
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__, template_folder='template')
# Creating a SocketIO instance.
socketio = SocketIO(app)
warnings.filterwarnings("ignore")


# convert function from https://github.com/NotCookey/Quote2Image
def convert(label, quote, author, fg, image, border_color, font_file=None, font_size=None, width=None, height=None):
    x1 = width if width else 612
    y1 = height if height else 612

    sentence = f"{quote} - {author}"

    quote = ImageFont.truetype(font_file if font_file else "fonts/Coves Bold.otf", font_size if font_size else 32)

    img = Image.new("RGB", (x1, y1), color=(255, 255, 255))

    back = Image.open(image, 'r')
    img_w, img_h = back.size
    bg_w, bg_h = img.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    bback = back.filter(ImageFilter.GaussianBlur(radius=1))
    img.paste(bback, offset)

    d = ImageDraw.Draw(img)

    sum = 0
    for letter in sentence:
        sum += d.textsize(letter, font=quote)[0]
    average_length_of_letter = sum / len(sentence)

    number_of_letters_for_each_line = (x1 / 1.618) / average_length_of_letter
    incrementer = 0
    fresh_sentence = ""

    for letter in sentence:
        if letter == "-":
            fresh_sentence += "\n\n" + letter + "\n\n"
        elif incrementer < number_of_letters_for_each_line:
            fresh_sentence += letter
        else:
            if letter == " ":
                fresh_sentence += "\n"
                incrementer = 0
            else:
                fresh_sentence += letter
        incrementer += 1
    dim = d.textsize(fresh_sentence, font=quote)
    x2 = dim[0]
    y2 = dim[1]

    qx = x1 / 2 - x2 / 2
    qy = y1 / 2 - y2 / 2

    d.text((820, 290), label, align="center", font=quote, fill=fg, )
    d.text((qx - 1, qy - 1), fresh_sentence, align="center", font=quote, fill=border_color)
    d.text((qx + 1, qy - 1), fresh_sentence, align="center", font=quote, fill=border_color)
    d.text((qx - 1, qy + 1), fresh_sentence, align="center", font=quote, fill=border_color)
    d.text((qx + 1, qy + 1), fresh_sentence, align="center", font=quote, fill=border_color)

    d.text((qx, qy), fresh_sentence, align="center", font=quote, fill=fg)

    return img


HitungWeton = HitungWeton()


@app.route("/")
def hello():
    return render_template('index.html')


#
# API Route
#
@app.route("/api", methods=['POST'])
def api():
    print('[ ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' ]  New Request API ' + request.remote_addr)
    nama_1 = request.form['nama_1']
    nama_2 = request.form['nama_2']
    date_1 = request.form['date_1']
    date_2 = request.form['date_2']

    if nama_1 == "" or nama_2 == "" or date_1 == "" or date_2 == "":
        return jsonify({"status": "error", "message": "Please fill all the fields"})

    if len(nama_1) > 15 or len(nama_2) > 15:
        return jsonify({"status": "error", "message": "Name is too long"})

    split_date1 = date_1.split("-")
    split_date2 = date_2.split("-")

    try:

        weton1 = HitungWeton.hitung(
            nama=nama_1,
            tahun=int(split_date1[0]),
            bulan=int(split_date1[1]),
            hari=int(split_date1[2])
        )

        weton2 = HitungWeton.hitung(
            nama=nama_2,
            tahun=int(split_date2[0]),
            bulan=int(split_date2[1]),
            hari=int(split_date2[2])
        )
        text = HitungWeton.keterangan_weton(weton1['jumlah_tambah'] + weton2['jumlah_tambah'])
        img = convert(
            label=text[0],
            quote=text[1],
            author=weton1['nama'] + " & " + weton2['nama'],
            fg="white",
            image="./asset/background.png",
            border_color="black",
            font_size=37,
            font_file="./asset/Coves Bold.otf",
            width=1748,
            height=1240
        )

        # Save The Image as a Png file
        img.save("./result.png", "PNG")

        # get the image from the server
        with open("./result.png", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            encoded_string = encoded_string.decode('utf-8')

        return jsonify({
            "status": "success",
            "data": {
                "weton_1": weton1,
                "weton_2": weton2,
                "nama_weton": text[0],
                "keterangan": text[1],
            },
            "image_base64": encoded_string
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


#
# SocketIO event handler
#
@socketio.on('connect')
def connect():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' Client connected')
    emit('connected', {'data': 'Connected to server'})


@socketio.on('start')
def start(message):
    try:
        print('[ ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' ]  New Data Received : ' + str(message))
        date_1 = message.get('data').get('date_1').split('-')
        date_2 = message.get('data').get('date_2').split('-')

        # check if date_1 is valid
        if len(date_1) != 3:
            emit('error', {'message': 'Date 1 is not valid'})
            return
        # check if date_2 is valid
        if len(date_2) != 3:
            emit('error', {'message': 'Date 2 is not valid'})
            return

        if message.get('data').get('nama_1') == '':
            emit('error', {'message': 'Nama 1 is empty'})
            return
        if message.get('data').get('nama_2') == '':
            emit('error', {'message': 'Nama 2 is empty'})
            return

        weton1 = HitungWeton.hitung(
            nama=message.get('data').get('nama_1'),
            tahun=int(date_1[0]),
            bulan=int(date_1[1]),
            hari=int(date_1[2])
        )

        weton2 = HitungWeton.hitung(
            nama=message.get('data').get('nama_2'),
            tahun=int(date_2[0]),
            bulan=int(date_2[1]),
            hari=int(date_2[2])
        )
        text = HitungWeton.keterangan_weton(weton1['jumlah_tambah'] + weton2['jumlah_tambah'])
        img = convert(
            label=text[0],
            quote=text[1],
            author=weton1['nama'] + " & " + weton2['nama'],
            fg="white",
            image="./asset/background.png",
            border_color="black",
            font_size=37,
            font_file="./asset/Coves Bold.otf",
            width=1748,
            height=1240
        )

        # Save The Image as a Png file
        img.save("./result.png", "PNG")

        # get the image from the server
        with open("./result.png", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            encoded_string = encoded_string.decode('utf-8')

        socketio.emit('image', {'image': encoded_string, 'status': 'success'})
    except Exception as e:
        print('[ ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' ] Error : ' + str(e))
        emit('error', {'message': 'Another Error'})
        return


if __name__ == '__main__':
    print("App Running on : http://localhost:5000")
    socketio.run(app, debug=False, log_output=False)
