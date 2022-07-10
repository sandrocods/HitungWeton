from src.HitungWeton import *

HitungWeton = HitungWeton()

weton1 = HitungWeton.hitung('s', 2001, 4, 12)

print("Hari Lahir Kamu : " + weton1['perhitungan']['nama_hari'])
print("Neptu Kamu : " + str(weton1['perhitungan']['hari_value']))
print("Pasaran Kamu : (" + str(weton1['perhitungan']['pasaran_value']) + ") " + weton1['perhitungan']['pasaran'] + "\n\n")

weton2 = HitungWeton.hitung('m', 2003, 4, 7)
print("Hari Lahir Pasangan Kamu : " + weton2['perhitungan']['nama_hari'])
print("Neptu Pasangan Kamu : " + str(weton2['perhitungan']['hari_value']))
print("Pasaran Pasangan Kamu : (" + str(weton2['perhitungan']['pasaran_value']) + ") " + weton2['perhitungan']['pasaran'] + "\n\n")

print("Jumlah Tambah : " + str(weton1['jumlah_tambah'] + weton2['jumlah_tambah']))

print(
    HitungWeton.keterangan_weton(weton1['jumlah_tambah'] + weton2['jumlah_tambah'])
)
