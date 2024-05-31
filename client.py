from datetime import datetime
from datetime import timedelta
import jsonrpclib

import logging

logging.basicConfig(level=logging.DEBUG)

# membuat stub pada client
s = jsonrpclib.Server('http://127.0.0.1:8081')

def select_menu():
    """ Menampilkan menu utama """
    global pilihan
    print('======= Selamat datang di Rumah Sakit Semangka! =======')
    print('1. Menampilkan daftar klinik yang buka')
    print('2. Menampilkan seluruh daftar klinik beserta jadwal dokter')
    print('3. Registrasi')
    print('4. Booking Antrian')
    print('0. Keluar')
    pilihan = input('Masukkan pilihan menu: ')
    while pilihan != '0':
        if pilihan == '1':
            tampil_daftar()
            return_menu()
        elif pilihan == '2':
            tampil_daftar_dokter()  # Memanggil method untuk menampilkan jadwal dokter dari server
            return_menu()
        elif pilihan == '3':
            registrasi()
            return_menu()
        elif pilihan == '4':
            booking()
            return_menu()
        else:
            print('Pilihan menu tidak sesuai, silahkan pilih kembali')
            print()
            select_menu()

def return_menu():
    """ Menampilkan menu untuk kembali ke menu utama """
    global pilihan
    print()
    kembali = input('Kembali ke menu utama? (Y/N): ')
    while kembali != 'Y' and kembali != 'y' and kembali != 'N' and kembali != 'n':
        kembali = input('Kembali ke menu utama? (Y/N): ')
    if kembali == 'Y' or kembali == 'y':
        print()
        select_menu()
    elif kembali == 'N' or kembali == 'n':
        pilihan = '0'

def tampil_daftar():
    """ Menampilkan daftar klinik yang buka saat program dijalankan """
    tgl = datetime.now()
    waktu = tgl.strftime("%H:%M")
    day = tgl.strftime("%d")
    # jika hari sudah berganti, maka data antrian pada seluruh klinik akan direset
    if day != s.get_hari():
        s.reset_antrian()
        s.set_hari(day)
    klinik_buka = s.get_klinik_buka(waktu)
    if klinik_buka:
        for klinik in klinik_buka:
            total_pasien = 0  # Inisialisasi total pasien
            for dokter in klinik['dokter']:
                # Menghitung total pasien untuk setiap hari dari semua dokter di klinik tersebut
                for antrian in dokter['antrian_hari'].values():
                    total_pasien += len(antrian)
            print('[', klinik['id'], ']', sep='')
            print('Nomor Klinik            :', klinik['id'])
            print('Nama Klinik             :', klinik['nama'])
            print('Jam Buka - Jam Tutup    :', klinik['buka'], '-', klinik['tutup'])
            print('Jumlah Pasien Terdaftar :', total_pasien)
            print()
    else:
        print('Tidak ada klinik yang buka')

def tampil_daftar_dokter():
    """ Memanggil method di server untuk menampilkan daftar klinik beserta jadwal dokter """
    daftar_dokter = s.tampil_daftar_dokter()
    print(daftar_dokter)

def time_in_range(start, end, current):
    """ Fungsi untuk mengecek apakah waktu current berada di antara waktu start dan end """
    start_time = datetime.strptime(start, "%H:%M").time()
    end_time = datetime.strptime(end, "%H:%M").time()
    current_time = datetime.strptime(current, "%H:%M").time()
    return start_time <= current_time <= end_time

def mapping_hari(hari):
        """ Mengubah nama hari dalam bahasa Indonesia """
        if hari == "Monday":
            return "Senin"
        elif hari == "Tuesday":
            return "Selasa"
        elif hari == "Wednesday":
            return "Rabu"
        elif hari == "Thursday":
            return "Kamis"
        elif hari == "Friday":
            return "Jumat"
        elif hari == "Saturday":
            return "Sabtu"
        elif hari == "Sunday":
            return "Minggu"

def registrasi():
    """ Fungsi untuk melakukan registrasi """
    # menerima input id klinik, selama tidak valid akan diminta input kembali
    while True:
        ids = input('Masukkan nomor klinik: ')
        while not ids in ['1', '2', '3', '4', '5']:
            print('Klinik tidak valid, silahkan pilih kembali')
            ids = input('Masukkan nomor klinik: ')
        id = int(ids)
        klinik = s.get_klinik(id)
        waktu_masuk = datetime.now()
        waktu = waktu_masuk.strftime("%H:%M")
        if not time_in_range(klinik['buka'], klinik['tutup'], waktu):
            print('Klinik tidak buka saat ini, silahkan pilih kembali')
        else:
            break
        
        
    day = waktu_masuk.strftime("%d")
    day_name = waktu_masuk.strftime("%A")
    day_name = mapping_hari(day_name)
    # jika hari sudah berganti, maka data antrian pada seluruh klinik akan direset
    if day != s.get_hari():
        s.reset_antrian()
        s.set_hari(day)
       
    # menerima input data pasien
    no_rekam_medis = input('Masukkan nomor rekam medis: ')
    nama = input('Masukkan nama: ')
    tgl_lahir = input('Masukkan tanggal lahir (dd-mm-yyyy): ')
    # memanggil fungsi regis() yang ada di komputer remote
    no_antri = s.regis(id, no_rekam_medis, nama, tgl_lahir, str(waktu_masuk), day_name)
    
    if no_antri == -1:
        print('Antrian Penuh')
        return
    else:
        # memanggil fungsi get_antri() yang ada di komputer remote
        antri = s.get_antri(id, no_antri, day_name)
        # menampilkan data antrian yang didapatkan
        print('-------------------------------------------------------')
        print('Nomor antrian:', antri['no'])
        print('Nama Dokter:', antri['dokter'])
        print('Antrian di depan Anda:', antri['antrian_di_depan'])
        # menghitung waktu giliran pasien masuk ke klinik
        print('Perkiraan waktu Anda mendapat giliran:', antri['waktu_masuk'] )
        print('Perkiraan waktu selesai:', antri['waktu_selesai'])

def booking():
    ids = input('Masukkan nomor klinik: ')
    while not ids in ['1', '2', '3', '4', '5']:
        print('Klinik tidak valid, silahkan pilih kembali')
        ids = input('Masukkan nomor klinik: ')
    id = int(ids)
    day_name = input('Masukkan hari (Senin, Selasa, Rabu, Kamis, Jumat, Sabtu): ')
    while not day_name in ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']:
        print('Hari tidak valid, silahkan pilih kembali')
        day_name = input('Masukkan hari (Senin, Selasa, Rabu, Kamis, Jumat, Sabtu): ')
    daftar_dokter = s.get_available_dokter(id, day_name)
    print('Dokter yang tersedia:\n1. '+ daftar_dokter[0] + '\n2. ' + daftar_dokter[1])
    no_dokter = input('Masukkan nomor dokter: ')
    while not no_dokter in ['1', '2']:
        print('Nomor dokter tidak valid, silahkan pilih kembali')
        no_dokter = input('Masukkan nomor dokter: ')
    no_rekam_medis = input('Masukkan nomor rekam medis: ')
    nama = input('Masukkan nama: ')
    tgl_lahir = input('Masukkan tanggal lahir (dd-mm-yyyy): ')
    antrian = s.booking(id, no_rekam_medis, nama, tgl_lahir, day_name, daftar_dokter[int(no_dokter)-1])
    if antrian == -1:
        print('Antrian Penuh')
        return
    else:
        # menampilkan data antrian yang didapatkan
        print('-------------------------------------------------------')
        print('Nomor antrian:', antrian['no'])
        print('Nama Dokter:', antrian['dokter'])
        print('Antrian di depan Anda:', antrian['antrian_di_depan'])
        print('Perkiraan waktu Anda mendapat giliran:', antrian['waktu_masuk'] )
        print('Perkiraan waktu selesai:', antrian['waktu_selesai'] )
    
    
# memanggil fungsi select_menu()
select_menu()
