##
# Author  : Sandroputraa
# Name    : Library Hitung Weton Jawa
# Build   : 09-07-2022
#
# If you are a reliable programmer or the best developer, please don't change anything.
# If you want to be appreciated by others, then don't change anything in this script.
# Please respect me for making this tool from the beginning.
##

from hijri_converter import Gregorian
from datetime import date


class HitungWeton:
    def __init__(self):
        pass

    def keterangan_weton(self, jumlah_tambah):
        array_keterangan = {
            "Pegat": "Dalam bahasa jawa berarti bercerai. Pasangan ini kemungkinan akan sering menghadapi masalah dikemudian hari. Masalah itu bisa dari masalah ekonomi, perselingkuhan, kekuasaan yang bisa menyebabkan perceraian.",

            "Ratu": "Identik dengan sosok yang dihormati. Pasangan ini bisa dikatakan sudah cocok dan berjodoh. Sangat dihargai dan disegani oleh tetangga maupun lingkungan sekitar. Bahkan tak sedikit orang sekitar yang iri dengan keharmonisannya dalam membina rumah tangga.",

            "Jodoh": "Pasangan ini memang ditakdirkan berjodoh. Mereka bisa saling menerima segala kekurangan maupun kelebihan masing2. Nasib rumah tangga dapat harmonis sampai tua.",

            "Topo": "Dalam bahasa jawa bisa diartikan bertirakat. Pasangan ini akan sering mengalami kesusahan di awal awal membina rumah tangga, namun pada akhirnya akan bahagia. Persoalan rumah tangga bisa dari ekonomi dan lain sebagainya. Tapi setelah mempunyai anak dan cukup lama berumah tangga, hidupnya akan sukses serta bahagia.",

            "Tinari": "Pasangan ini akan mendapatkan kebahagiaan. Kemudahan dalam mencari rezeki dan tidak akan hidup berkekurangan. Hidupnya juga diliputi keberuntungan.",

            "Padu": "Padu dalam bahasa jawa berarti cekcok atau pertengkaran. Rumah tangga pasangan ini akan sering mengalami pertikaian atau pertengkaran. Meski sering terjadi pertengkaran, nasib rumah tangga tidak sampai bercerai. Pertengkaran ini bahkan dipicu dari hal hal yang bersifat sepele.",

            "Sujanan": "Rumah tangga ini akan sering mengalami percekcokan dan masalah perselingkuhan.",

            "Pesthi": "Rumah tangga akan berjalan dengan sangat harmonis, rukun, adem, ayem, tenteram dan sejahtera sampai tua. Bisa dikatakan jika ada sedikit masalah namun tidak megganggu keharmonisan.",
        }

        if jumlah_tambah in [1, 9, 10, 18, 19, 27, 28, 36]:
            return "Pegat", array_keterangan['Pegat']
        elif jumlah_tambah in [2, 11, 20, 29]:
            return "Ratu", array_keterangan['Ratu']
        elif jumlah_tambah in [3, 12, 21, 30]:
            return "Jodoh", array_keterangan['Jodoh']
        elif jumlah_tambah in [4, 13, 22, 31]:
            return "Topo", array_keterangan['Topo']
        elif jumlah_tambah in [5, 14, 23, 32]:
            return "Tinari", array_keterangan['Tinari']
        elif jumlah_tambah in [6, 15, 24, 33]:
            return "Padu", array_keterangan['Padu']
        elif jumlah_tambah in [7, 16, 25, 34]:
            return "Sujanan", array_keterangan['Sujanan']
        elif jumlah_tambah in [8, 17, 26, 35]:
            return "Pesthi", array_keterangan['Pesthi']

    def get_day_of_week(self, julian_date):
        day_of_week = julian_date % 7
        return day_of_week + 1

    def hitung_tanggal(self, tahun, bulan, hari):
        julian_date = date(tahun, bulan, hari).toordinal() + 1721425
        day_of_week = self.get_day_of_week(julian_date)
        result = Gregorian(tahun, bulan, hari).to_hijri()

        self.day_of_week = day_of_week
        self.hijri_day = result.day
        self.hijri_month = result.month
        self.hijri_year = result.year
        self.java_year = result.year + 512
        self.java_dow = (julian_date + 3) % 5
        return {
            'day_of_week': day_of_week,
            'hijri_day': result.day,
            'hijri_month': result.month,
            'hijri_year': result.year,
            'java_year': result.year + 512,
            'java_dow': (julian_date + 3) % 5,
        }

    def konversi(self):
        global day_of_week, pasaran
        array_hari = {
            'Minggu': 5,
            'Senin': 4,
            'Selasa': 3,
            'Rabu': 7,
            'Kamis': 8,
            'Jumat': 6,
            'Sabtu': 9
        }
        i_day_array = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
        array_jawa_day = ['Pon', 'Wage', 'Kliwon', 'Legi', 'Pahing']
        array_pasaran = {
            'Legi': 5,
            'Pahing': 9,
            'Pon': 7,
            'Wage': 4,
            'Kliwon': 8,
        }

        result = self.hitung_tanggal(self.tahun, self.bulan, self.hari)

        for i, j in array_hari.items():

            if i_day_array[result['day_of_week']] == i:
                day_of_week = j
                break

        pasaran = None
        for i, j in array_pasaran.items():
            if array_jawa_day[result['java_dow']] == i:
                pasaran = j
                break

        jumlah_tambah = day_of_week + pasaran

        return {
            'nama_hari': i_day_array[result['day_of_week']],
            'hari_value': day_of_week,
            'pasaran': array_jawa_day[result['java_dow']],
            'pasaran_value': pasaran,
            'jumlah_tambah': jumlah_tambah,

        }

    def hitung(self, nama, tahun, bulan, hari):
        """
        It takes in a name, year, month, and day, and returns a dictionary with the name, the date, the calculation, and the
        sum of the calculation

        :param nama: name of the person
        :param tahun: year
        :param bulan: month
        :param hari: The day of the month (1-31)
        """
        self.nama = nama
        self.tahun = tahun
        self.bulan = bulan
        self.hari = hari

        return {
            'nama': nama,
            'data': self.hitung_tanggal(tahun, bulan, hari),
            'perhitungan': self.konversi(),
            'jumlah_tambah': self.konversi()['jumlah_tambah'],
        }
