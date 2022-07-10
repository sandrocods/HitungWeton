import warnings
from src.HitungWeton import *
from PIL import Image, ImageDraw, ImageFont, ImageFilter

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

weton1 = HitungWeton.hitung(
    nama='s',
    tahun=2001,
    bulan=4,
    hari=12
)

print("Hari Lahir Kamu : " + weton1['perhitungan']['nama_hari'])
print("Neptu Kamu : " + str(weton1['perhitungan']['hari_value']))
print(
    "Pasaran Kamu : (" + str(weton1['perhitungan']['pasaran_value']) + ") " + weton1['perhitungan']['pasaran'] + "\n\n")

weton2 = HitungWeton.hitung(
    nama='m',
    tahun=2003,
    bulan=4,
    hari=7
)

print("Hari Lahir Pasangan Kamu : " + weton2['perhitungan']['nama_hari'])
print("Neptu Pasangan Kamu : " + str(weton2['perhitungan']['hari_value']))
print("Pasaran Pasangan Kamu : (" + str(weton2['perhitungan']['pasaran_value']) + ") " + weton2['perhitungan'][
    'pasaran'] + "\n\n")

print("Jumlah Tambah : " + str(weton1['jumlah_tambah'] + weton2['jumlah_tambah']))

print(
    HitungWeton.keterangan_weton(weton1['jumlah_tambah'] + weton2['jumlah_tambah'])
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
if img.save("./result.png", "PNG"):
    print("Image saved successfully")
