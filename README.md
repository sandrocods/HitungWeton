
# HitungWetonPy

Hitung Weton Py adalah library Python3 yang dibuat untuk meghitung weton dan maknanya sesuai dengan neptu dan pasaran yang ada di pulau Jawa, Pemahaman ini tidak bisa dijadikan patokan utama dalam kehidupan sehari-hari. Tergantung dari sisi kepercayaan masing-masing.




## 🚀 Demo

Untuk demo bisa klik link dibawah

[Demo Aplikasi Hitung Weton Versi WEB ](http://20.243.8.47/)



## 📝 Dibuat Dengan

 - [Python3](https://www.python.org/downloads/)
 - [hijri-converter](https://pypi.org/project/hijri-converter/)
 - [Flask](https://pypi.org/project/Flask/)
 - [Flask-SocketIO](https://pypi.org/project/Flask-SocketIO/)
 - [Pillow](https://pypi.org/project/Pillow/)
 
## 🔰 Fitur

| Fitur             |  | File |
| ----------------- | -- |-- |
| Perhitungan Weton CLI | ✅ | [Example_CLI.py](https://github.com/sandrocods/HitungWeton/blob/master/Example_CLI.py) |
| Perhitungan Weton + Generate Quotes | ✅ | [Example_Photo.py](https://github.com/sandrocods/HitungWeton/blob/master/Example_Photo.py) |
| Perhitungan Weton WEB Realtime + API | ✅ | [Example_Flask.py](https://github.com/sandrocods/HitungWeton/blob/master/Example_Flask.py) |


## ➕ Instalasi

Untuk menggunakan Library ini ada beberapa langkah instalasi

```bash
  // Git Repository dan masuk ke folder project

  git clone https://github.com/sandrocods/HitungWeton
  cd HitungWeton
```

```bash
  // Install reqruitments dan menjalankan example code program
  
  pip3 install -r ./requirments.txt
  python3 Example_CLI.py
```



## 📚 Contoh

Penggunaan Library HitungWetonPy


#### Import Library

```python
  from src.HitungWeton import *
```

#### Membuat Instance dari class HitungWeton

```python
  HitungWeton = HitungWeton()
```

#### Hitung Weton 1
```python
weton1 = HitungWeton.hitung(nama, tahun, bulan, hari)

```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `nama`      | `string` | **optional**. Memberi nama weton1 |
| `tahun`      | `integer` | **required**. Tahun Lahir |
| `bulan`      | `integer` | **required**. Bulan Lahir |
| `hari`      | `integer` | **required**. Hari Lahir |

### Result :
Menghasilkan result Day of Week , Hari bulan tahun Hijriah dan tahun Jawa lengkap dengan pasaran dan neptunya
```json

{
    "nama": "sds",
    "data": {
        "day_of_week": 4,
        "hijri_day": 18,
        "hijri_month": 1,
        "hijri_year": 1422,
        "java_year": 1934,
        "java_dow": 0
    },
    "perhitungan": {
        "nama_hari": "Kamis",
        "hari_value": 8,
        "pasaran": "Pon",
        "pasaran_value": 7,
        "jumlah_tambah": 15
    },
    "jumlah_tambah": 15
}

```

Untuk Mengetahui Keterangan kecocokan pasangan menggunakan 2 weton yang ditambahkan menjadi satu

#### Hitung Weton 1 dan Weton 2
```python

keterangan = weton1['jumlah_tambah'] + weton2['jumlah_tambah']

```

### Result :

```json

[
    "Pesthi",
    "Rumah tangga akan berjalan dengan sangat harmonis, rukun, adem, ayem, tenteram dan sejahtera sampai tua. Bisa dikatakan jika ada sedikit masalah namun tidak megganggu keharmonisan."
]

```


## 🌐 Penggunaan Versi Web

#### Di versi web ini langsung mengeluarkan output gambar yang telah digenerate nama dan keterangan weton dalam format base64

Untuk public production menggunakan VPS disarankan Menggunakan uWSGI 
karena pada project ini memakai libaray FlaskSocketIO untuk update realtimenya

! pastikan requirments sudah terinstall semua 

```bash
  uwsgi --http :80 --gevent 1000 --http-websockets --master --wsgi-file Example_Flask.py --callable app
```
### Result :
![app](https://i.ibb.co/XLZHtXN/image.png)

Untuk penggunaan local bisa langsung menjalankan command dibawah

```bash
    $env:FLASK_APP = "Example_Flask.py"
    flask run
```

### Result :
![app](https://i.ibb.co/9rBC6X4/image.png)


## 🔥Refrensi API

```http
  POST {{base_url}}/api/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `nama_1`      | `string` | **required**. Memberi nama weton1 |
| `date_1`      | `string` | **required**. Tahun Lahir, example : 2001-04-12 |
| `nama_2`      | `string` | **required**. Memberi nama weton2 |
| `date_2`      | `string` | **required**. Tahun Lahir, example : 2003-04-07 |

#### Response Sukses : 

```json
{
	"data": {
		"keterangan": "Rumah tangga akan berjalan dengan sangat harmonis, rukun, adem, ayem, tenteram dan sejahtera sampai tua. Bisa dikatakan jika ada sedikit masalah namun tidak megganggu keharmonisan.",
		"nama_weton": "Pesthi",
		"weton_1": {
			"data": {
				"day_of_week": 4,
				"hijri_day": 18,
				"hijri_month": 1,
				"hijri_year": 1422,
				"java_dow": 0,
				"java_year": 1934
			},
			"jumlah_tambah": 15,
			"nama": "S",
			"perhitungan": {
				"hari_value": 8,
				"jumlah_tambah": 15,
				"nama_hari": "Kamis",
				"pasaran": "Pon",
				"pasaran_value": 7
			}
		},
		"weton_2": {
			"data": {
				"day_of_week": 1,
				"hijri_day": 5,
				"hijri_month": 2,
				"hijri_year": 1424,
				"java_dow": 0,
				"java_year": 1936
			},
			"jumlah_tambah": 11,
			"nama": "M",
			"perhitungan": {
				"hari_value": 4,
				"jumlah_tambah": 11,
				"nama_hari": "Senin",
				"pasaran": "Pon",
				"pasaran_value": 7
			}
		}
	},
	"image_base64": "i.......K5CYII=",
	"status": "success"
}
```



#### Response Error : 

```json

// Belum mengisi semua parameter POST data
{
	"message": "Please fill all the fields",
	"status": "error"
}

// Tanggal tidak valid
{
	"message": "list index out of range",
	"status": "error"
}

{
	"message": "day is out of range for month",
	"status": "error"
}

// Nama terlalu panjang
{
	"message": "Name is too long",
	"status": "error"
}

```
## 📷 Screenshots
Example_CLI.py

![App Screenshot](https://i.ibb.co/1sWm32C/image.png)

Example_Photo.py

![App](https://im3.ezgif.com/tmp/ezgif-3-3a546823f1.gif)

Example_Flask.py

![App](https://i.ibb.co/kMYRrY1/image.png)

## 😉 Authors

- [@sandrocods](https://www.github.com/sandrocods)



## 🙌 Support

Jika anda menyukai Project ini silahkan klik start project , 
masih banyak kekurangan bisa submit issue atau langsung hubungi saya melalui telegram
https://t.me/Sandroputraaa

