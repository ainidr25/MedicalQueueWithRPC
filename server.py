# server.py

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from datetime import datetime
from datetime import timedelta

import logging

logging.basicConfig(level=logging.DEBUG)

# Membuat server
server = SimpleJSONRPCServer(("127.0.0.1", 8081))
server.register_introspection_functions()
print("Server running on")

def time_in_range(start, end, x):
    """ Mengembalikan True jika x berada dalam range [start, end] """
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end
    
def get_date(day):
        # Mendefinisikan hari-hari dalam seminggu
        days_of_week = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
        
        # Mendapatkan hari ini
        today = datetime.now()
        
        # Mendapatkan indeks hari ini dan hari yang diinginkan
        today_index = today.weekday()
        target_index = days_of_week.index(day)
        
        # Menghitung perbedaan hari
        day_difference = (target_index - today_index) % 7
        
        # Jika hari yang diinginkan adalah hari ini, kita tidak perlu menambahkan hari
        if day_difference == 0:
            return str(today)
        
        # Menghitung tanggal hari yang diinginkan
        target_date = today + timedelta(days=day_difference)
        
        return str(target_date)
    

# Membuat instansiasi yang dipublikasikan sebagai method XML-RPC
# waktu_pasien dalam format menit
daftar_klinik = [
    {
        "id": 1,
        "nama": "Poli Gigi",
        "buka": "09:00",
        "tutup": "19:00",
        "waktu_pasien": 30,
        "dokter": [
			{
				"nama": "dr. Mentari",
				"hari_kerja": ["Senin", "Rabu", "Jumat"],
				"jam_awal_kerja": "09:00",
				"jam_akhir_kerja": "13:00",
                "antrian_hari": {"Senin": [], "Rabu": [], "Jumat": []},
                "jml_antrian_hari": {"Senin": 0, "Rabu": 0, "Jumat": 0}
			},
			{
				"nama": "dr. Yanti",
				"hari_kerja": ["Selasa", "Kamis", "Sabtu"],
				"jam_awal_kerja": "09:00",
				"jam_akhir_kerja": "11:00",
                "antrian_hari": {"Selasa": [], "Kamis": [], "Sabtu": []},
                "jml_antrian_hari": {"Selasa": 0, "Kamis": 0, "Sabtu": 0}
			},
			{
				"nama": "dr. Yadi",
				"hari_kerja": ["Senin", "Rabu", "Jumat"],
				"jam_awal_kerja": "13:00",
				"jam_akhir_kerja": "19:00",
                "antrian_hari": {"Senin": [], "Rabu": [], "Jumat": []},
                "jml_antrian_hari": {"Senin": 0, "Rabu": 0, "Jumat": 0}
                
			},		
			{
				"nama": "dr. Anto",
				"hari_kerja": ["Selasa", "Kamis", "Sabtu"],
				"jam_awal_kerja": "11:00",
				"jam_akhir_kerja": "19:00",
                "antrian_hari": {"Selasa": [], "Kamis": [], "Sabtu": []},
                "jml_antrian_hari": {"Selasa": 0, "Kamis": 0, "Sabtu": 0}
			},				
			
		]
    },
    {
        "id": 2,
        "nama": "Poli Mata",
        "buka": "09:00",
        "tutup": "18:00",
        "waktu_pasien": 15,
        "dokter": [
			{
				"nama": "dr. Azis",
				"hari_kerja": ["Senin", "Rabu", "Kamis  "],
				"jam_awal_kerja": "09:00",
				"jam_akhir_kerja": "13:30",
                "antrian_hari": {"Senin": [], "Rabu": [], "Kamis": []},
                "jml_antrian_hari": {"Senin": 0, "Rabu": 0, "Kamis": 0}
			},
			{
				"nama": "dr. Ayu",
				"hari_kerja": ["Selasa", "Jumat", "Sabtu"],
				"jam_awal_kerja": "09:00",
				"jam_akhir_kerja": "13:00",
                "antrian_hari": {"Selasa": [], "Jumat": [], "Sabtu": []},
                "jml_antrian_hari": {"Selasa": 0, "Jumat": 0, "Sabtu": 0}
			},
			{
				"nama": "dr. Sinta",
				"hari_kerja": ["Senin", "Rabu", "Kamis  "],
				"jam_awal_kerja": "13:30",
				"jam_akhir_kerja": "18:00",
                "antrian_hari": {"Senin": [], "Rabu": [], "Kamis": []},
                "jml_antrian_hari": {"Senin": 0, "Rabu": 0, "Kamis": 0}
			},		
			{
				"nama": "dr. Anto",
				"hari_kerja": ["Selasa", "Jumat", "Sabtu"],
				"jam_awal_kerja": "13:00",
				"jam_akhir_kerja": "18:00",
                "antrian_hari": {"Selasa": [], "Jumat": [], "Sabtu": []},
                "jml_antrian_hari": {"Selasa": 0, "Jumat": 0, "Sabtu": 0}
			},	
		]
    },
    {
        "id": 3,
        "nama": "Poli Saraf",
        "buka": "08:00",
        "tutup": "17:00",
        "waktu_pasien": 50,
        "dokter": [
			{
				"nama": "dr. Delvito",
				"hari_kerja": ["Senin", "Rabu", "Jumat"],
				"jam_awal_kerja": "08:00",
				"jam_akhir_kerja": "12:00",
                "antrian_hari": {"Senin": [], "Rabu": [], "Jumat": []},
                "jml_antrian_hari": {"Senin": 0, "Rabu": 0, "Jumat": 0}
			},
			{
				"nama": "dr. Asep",
				"hari_kerja": ["Selasa", "Kamis", "Sabtu"],
				"jam_awal_kerja": "08:00",
				"jam_akhir_kerja": "12:00",
                "antrian_hari": {"Selasa": [], "Kamis": [], "Sabtu": []},
                "jml_antrian_hari": {"Selasa": 0, "Kamis": 0, "Sabtu": 0}
			},
			{
				"nama": "dr. Santy",
				"hari_kerja": ["Senin", "Rabu", "Jumat"],
				"jam_awal_kerja": "12:00",
				"jam_akhir_kerja": "17:00",
                "antrian_hari": {"Senin": [], "Rabu": [], "Jumat": []},
                "jml_antrian_hari": {"Senin": 0, "Rabu": 0, "Jumat": 0}
			},		
			{
				"nama": "dr. Floresia",
				"hari_kerja": ["Selasa", "Kamis", "Sabtu"],
				"jam_awal_kerja": "12:00",
				"jam_akhir_kerja": "17:00",
                "antrian_hari": {"Selasa": [], "Kamis": [], "Sabtu": []},
                "jml_antrian_hari": {"Selasa": 0, "Kamis": 0, "Sabtu": 0}
			},	
		]
    },
    {
        "id": 4,
        "nama": "Poli Anak",
        "buka": "07:00",
        "tutup": "18:00",
        "waktu_pasien": 20,
        "dokter": [
			{
				"nama": "dr. Aini",
				"hari_kerja": ["Senin", "Rabu", "Kamis  "],
				"jam_awal_kerja": "07:00",
				"jam_akhir_kerja": "13:00",
                "antrian_hari": {"Senin": [], "Rabu": [], "Kamis": []},
                "jml_antrian_hari": {"Senin": 0, "Rabu": 0, "Kamis": 0}
			},
			{
				"nama": "dr. Budi",
				"hari_kerja": ["Selasa", "Jumat", "Sabtu"],
				"jam_awal_kerja": "07:00",
				"jam_akhir_kerja": "13:00",
                "antrian_hari": {"Selasa": [], "Jumat": [], "Sabtu": []},
                "jml_antrian_hari": {"Selasa": 0, "Jumat": 0, "Sabtu": 0}
			},
			{
				"nama": "dr. Soni",
				"hari_kerja": ["Senin", "Rabu", "Kamis  "],
				"jam_awal_kerja": "13:00",
				"jam_akhir_kerja": "18:00",
                "antrian_hari": {"Senin": [], "Rabu": [], "Kamis": []},
                "jml_antrian_hari": {"Senin": 0, "Rabu": 0, "Kamis": 0}
			},		
			{
				"nama": "dr. Laurence",
				"hari_kerja": ["Selasa", "Jumat", "Sabtu"],
				"jam_awal_kerja": "13:00",
				"jam_akhir_kerja": "18:00",
                "antrian_hari": {"Selasa": [], "Jumat": [], "Sabtu": []},
                "jml_antrian_hari": {"Selasa": 0, "Jumat": 0, "Sabtu": 0}
			},	
		]
    },
    {
        "id": 5,
        "nama": "Poli Jantung",
        "buka": "08:00",
        "tutup": "17:00",
        "waktu_pasien": 50,
        "dokter": [
			{
				"nama": "dr. Rafi",
				"hari_kerja": ["Senin", "Rabu", "Jumat"],
				"jam_awal_kerja": "08:00",
				"jam_akhir_kerja": "12:00",
                "antrian_hari": {"Senin": [], "Rabu": [], "Jumat": []},
                "jml_antrian_hari": {"Senin": 0, "Rabu": 0, "Jumat": 0}
			},
			{
				"nama": "dr. Rachmat",
				"hari_kerja": ["Selasa", "Kamis", "Sabtu"],
				"jam_awal_kerja": "08:00",
				"jam_akhir_kerja": "12:00",
                "antrian_hari": {"Selasa": [], "Kamis": [], "Sabtu": []},
                "jml_antrian_hari": {"Selasa": 0, "Kamis": 0, "Sabtu": 0}
			},
			{
				"nama": "dr. Alysia",
				"hari_kerja": ["Senin", "Rabu", "Jumat"],
				"jam_awal_kerja": "12:00",
				"jam_akhir_kerja": "17:00",
                "antrian_hari": {"Senin": [], "Rabu": [], "Jumat": []},
                "jml_antrian_hari": {"Senin": 0, "Rabu": 0, "Jumat": 0}
			},		
			{
				"nama": "dr. Saldy",
				"hari_kerja": ["Selasa", "Kamis", "Sabtu"],
				"jam_awal_kerja": "12:00",
				"jam_akhir_kerja": "17:00",
                "antrian_hari": {"Selasa": [], "Kamis": [], "Sabtu": []},
                "jml_antrian_hari": {"Selasa": 0, "Kamis": 0, "Sabtu": 0}
			},	
		]
    }
]
pertama = True  # variabel yang bernilai True jika pasien merupakan pasien pertama yang melakukan registrasi pada sistem
tgl_hari_ini = ''

class RumahSakit:
    def get_klinik(self, id):
        """Diberikan sebuah bilangan bulat id untuk mengembalikan data klinik yang memiliki id tersebut jika ada,
        jika tidak akan mengembalikan -1"""
        global daftar_klinik
        for klinik in daftar_klinik:
            if klinik['id'] == id:
                return klinik
        return -1

    def regis(self, id, no_rekam_medis, nama, tgl_lahir, waktu_masuk, day):
        """Menyimpan data pasien yang melakukan registrasi pada klinik tertentu, dan mengembalikan nomor antrian
        yang didapat"""
        global daftar_klinik
        datetime_waktu_masuk = datetime.strptime(waktu_masuk, '%Y-%m-%d %H:%M:%S.%f')
        jam = datetime_waktu_masuk.strftime("%H:%M")
        for klinik in daftar_klinik:
            
            if klinik['id'] == id:
                antrian_baru = {
                    'no': None,  # Nomor antrian akan diatur nanti
                    'no_rekam_medis': no_rekam_medis,
                    'nama': nama,
                    'tgl_lahir': tgl_lahir,
                    'waktu_masuk': waktu_masuk,
                    'waktu_selesai': None,
                    'dokter': None,
                    'antrian_di_depan': None
                }
                
                for dokter in klinik['dokter']:
                    is_dokter_praktik = self.get_dokter_praktik(id, jam, dokter['nama'])
                    if day in dokter['hari_kerja'] and is_dokter_praktik:
                        str_waktu_antrian = self.get_waktu_antrian(id, day, dokter['nama'])
                        waktu_antrian = None
                        jam_antrian = None
                        if str_waktu_antrian == "Antrian Kosong":
                            waktu_antrian = datetime.now()
                            jam_antrian = waktu_antrian.strftime("%H:%M")
                        else:
                            waktu_antrian = datetime.strptime(str_waktu_antrian, '%Y-%m-%d %H:%M:%S.%f')
                            jam_antrian = waktu_antrian.strftime("%H:%M")
                        is_masih_ada_antrian = self.get_dokter_praktik(id, jam_antrian, dokter['nama'])
                        if is_masih_ada_antrian:
                            antrian_baru['no'] = len(dokter['antrian_hari'][day]) + 1
                            waktu_selesai = waktu_antrian + timedelta(minutes=klinik['waktu_pasien'])
                            antrian_baru['waktu_masuk'] = str(waktu_antrian)
                            antrian_baru['waktu_selesai'] = str(waktu_selesai)
                            antrian_baru['dokter'] = dokter['nama']
                            dokter['antrian_hari'][day].append(antrian_baru)
                            antrian_baru['antrian_di_depan'] = len(dokter['antrian_hari'][day]) - 1
                            return antrian_baru
                        else:
                            return -1
        return None  # Jika tidak ada klinik atau dokter yang cocok
    
    def booking(self, id, no_rekam_medis, nama, tgl_lahir, hari_booking, dokter_dipilih):
        """Menyimpan data pasien yang melakukan registrasi pada klinik tertentu, dan mengembalikan nomor antrian
        yang didapat"""
        global daftar_klinik
        waktu_masuk = get_date(hari_booking)
        for klinik in daftar_klinik:
            if klinik['id'] == id:
                antrian_baru = {
                    'no': None,  # Nomor antrian akan diatur nanti
                    'no_rekam_medis': no_rekam_medis,
                    'nama': nama,
                    'tgl_lahir': tgl_lahir,
                    'waktu_masuk': waktu_masuk,
                    'waktu_selesai': None,
                    'dokter': dokter_dipilih,
                    'antrian_di_depan': None
                }
                for dokter in klinik['dokter']:
                    if dokter['nama'] == dokter_dipilih:
                        str_waktu_antrian_terakhir = self.get_waktu_antrian(id, hari_booking, dokter['nama'])
                        waktu_antrian = None
                        if str_waktu_antrian_terakhir == "Antrian Kosong":
                            str_waktu_antrian = get_date(hari_booking)
                            waktu_antrian = datetime.strptime(str_waktu_antrian, '%Y-%m-%d %H:%M:%S.%f')
                            jam_awal_kerja = datetime.strptime(dokter['jam_awal_kerja'], '%H:%M')
                            waktu_antrian = waktu_antrian.replace(hour=jam_awal_kerja.hour, minute=jam_awal_kerja.minute)
                            #jika waktu_masuk lebih kecil dari waktu sekarang, maka waktu_masuk di tambah 7 hari
                            if waktu_antrian < datetime.now():
                                waktu_antrian = waktu_antrian + timedelta(days=7)
                        else:
                            waktu_antrian = datetime.strptime(str_waktu_antrian_terakhir, '%Y-%m-%d %H:%M:%S.%f')
                        jam_antrian = waktu_antrian.strftime("%H:%M")
                        is_masih_ada_antrian = self.get_dokter_praktik(id, jam_antrian, dokter['nama'])
                        if is_masih_ada_antrian:
                            antrian_baru['no'] = len(dokter['antrian_hari'][hari_booking]) + 1
                            waktu_selesai = waktu_antrian + timedelta(minutes=klinik['waktu_pasien'])
                            antrian_baru['waktu_selesai'] = str(waktu_selesai)
                            antrian_baru['dokter'] = dokter['nama']
                            antrian_baru['waktu_masuk'] = str(waktu_antrian)
                            dokter['antrian_hari'][hari_booking].append(antrian_baru)
                            antrian_baru['antrian_di_depan'] = len(dokter['antrian_hari'][hari_booking]) - 1
                            return antrian_baru
                        else:
                            return -1
        return None  # Jika tidak ada klinik atau dokter yang cocok
        

    def get_antri(self, id, no, day):
        """Diberikan sebuah bilangan bulat 'id' dan 'no', untuk mengembalikan data antrian dengan nomor 'no' pada klinik
        dengan id = 'id'"""
        global daftar_klinik
        for klinik in daftar_klinik:
            if klinik['id'] == id:
                for dokter in klinik['dokter']:
                    for antrian in dokter['antrian_hari'][day]:
                        if antrian['no'] == no:
                            return antrian
        return None

    def get_klinik_buka(self, waktu):
        """Mengembalikan daftar klinik yang buka pada saat 'waktu'"""
        global daftar_klinik
        klinik_buka = []
        for klinik in daftar_klinik:
            if time_in_range(klinik['buka'], klinik['tutup'], waktu):
                klinik_buka.append(klinik)
        return klinik_buka
    
    def get_dokter_praktik(self, id, waktu, dokter):
        """Mengembalikan True jika dokter 'dokter' bekerja pada hari 'hari' pada klinik dengan id 'id' pada saat 'waktu'"""
        global daftar_klinik
        for klinik in daftar_klinik:
            if klinik['id'] == id:
                for dokter_klinik in klinik['dokter']:
                    if dokter_klinik['nama'] == dokter:
                        if time_in_range(dokter_klinik['jam_awal_kerja'], dokter_klinik['jam_akhir_kerja'], waktu):
                            return True
        return False

    def reset_antrian(self):
        """Menghapus data pada list antrian dan mengeset jumlah pasien menjadi 0 pada seluruh klinik"""
        global daftar_klinik
        for klinik in daftar_klinik:
            for dokter in klinik['dokter']:
                for hari in dokter['hari_kerja']:
                    dokter['antrian_hari'][hari] = []

    def get_hari(self):
        """Mengembalikan tanggal hari ini"""
        global pertama, tgl_hari_ini
        if pertama:
            tgl_hari_ini = datetime.now().strftime("%d")
            pertama = False
        return tgl_hari_ini

    def set_hari(self, tgl):
        """Mengeset tanggal hari ini dengan nilai dari 'tgl'"""
        global tgl_hari_ini
        tgl_hari_ini = tgl

    def tampil_daftar_dokter(self):
        """Menampilkan seluruh daftar klinik beserta jadwal dokter"""
        global daftar_klinik
        daftar_str = ""
        for klinik in daftar_klinik:
            daftar_str += "==================================================\n"
            daftar_str += f"||\t\tKlinik : {klinik['nama']}\t\t||\n"
            daftar_str += "++++++++++++++++++++++++++++++++++++++++++++++++++\n"
            daftar_str += "|\t\t    Jadwal Dokter   \t\t |\n"

            dokter_counter = 1
            for dokter in klinik['dokter']:
                daftar_str += f"| {dokter_counter}. Nama Dokter  : {dokter['nama']} \t\t |\n"
                daftar_str += f"|    Hari Kerja  : {', '.join(dokter['hari_kerja'])}\t\t |\n"
                daftar_str += f"|    Jam Kerja   : {dokter['jam_awal_kerja']} - {dokter['jam_akhir_kerja']}\t\t |\n"
                daftar_str += "|\t\t\t\t\t\t |\n"
                dokter_counter += 1

            daftar_str += "==================================================\n\n"
        return daftar_str

    def get_available_dokter(self, id, hari):
        """Mengembalikan daftar dokter yang bekerja pada hari 'hari' pada klinik dengan id 'id'"""
        global daftar_klinik
        for klinik in daftar_klinik:
            if klinik['id'] == id:
                dokter_hari = []
                for dokter in klinik['dokter']:
                    if hari in dokter['hari_kerja']:
                        dokter_hari.append(dokter['nama'])
                return dokter_hari
        return None
    
    def get_waktu_antrian(self, id, hari, dokter):
        """Mengembalikan waktu antrian terakhir yang terdaftar pada dokter 'dokter' pada hari 'hari' pada klinik dengan id 'id'"""
        global daftar_klinik
        for klinik in daftar_klinik:
            if klinik['id'] == id:
                for dokter_klinik in klinik['dokter']:
                    if dokter_klinik['nama'] == dokter:
                        # cek apakah dokter_klinik['antrian_hari'][hari] kosong
                        if dokter_klinik['antrian_hari'][hari]:
                            antrian_terakhir = dokter_klinik['antrian_hari'][hari][-1]
                            return antrian_terakhir['waktu_selesai']
                        else:
                            return "Antrian Kosong"
        return None

    
# meregisterkan class pada server
server.register_instance(RumahSakit())

# menjalankan server
server.serve_forever()
