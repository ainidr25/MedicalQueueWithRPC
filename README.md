# Sistem Antrian Registrasi Medis

Proyek ini adalah implementasi sistem antrian registrasi medis yang memanfaatkan mekanisme RPC (Remote Procedure Call) untuk meningkatkan efisiensi dan pengalaman pasien di rumah sakit.

## Deskripsi

Sistem "Antrian Registrasi Medis" ini bertujuan untuk memfasilitasi pasien dalam melakukan proses pendaftaran dan penjadwalan kedatangan (booking antrian) di rumah sakit. Dengan sistem ini, pasien dapat mengurangi waktu tunggu dan melakukan registrasi atau booking antrian secara cepat dan efisien ke klinik yang diinginkan.

## Fitur Utama

1. **Menampilkan Daftar Klinik yang Buka**: Pengguna dapat melihat daftar klinik yang buka berdasarkan waktu akses aplikasi.
2. **Menampilkan Seluruh Daftar Klinik dan Jadwal Dokter**: Menampilkan informasi lengkap mengenai klinik dan jadwal dokter yang tersedia.
3. **Registrasi Pasien**: Memungkinkan pasien untuk melakukan registrasi secara online tanpa harus menunggu di rumah sakit.
4. **Booking Antrian**: Memungkinkan pasien untuk melakukan penjadwalan janji temu dengan dokter di klinik tertentu.

## Arsitektur Sistem

Sistem ini terdiri dari dua komponen utama:
- **Server**: Menangani logika bisnis dan penyimpanan data.
- **Client**: Antarmuka pengguna untuk berinteraksi dengan sistem.

### Teknologi yang Digunakan

- **Bahasa Pemrograman**: Python
- **Library**: 
  - jsonrpclib
  - datetime
  - logging

### Arsitektur Jaringan

Sistem menggunakan arsitektur client-server di mana client mengirim permintaan ke server melalui protokol HTTP yang kemudian diproses oleh server menggunakan mekanisme RPC.

## Instalasi

1. Clone repositori ini:
    ```bash
    git clone https://github.com/ainidr25/MedicalQueueWithRPC.git
    ```
2. Masuk ke direktori proyek:
    ```bash
    cd MedicalQueueWithRPC
    ```

## Penggunaan

1. Jalankan server:
    ```bash
    python server.py
    ```
2. Jalankan client:
    ```bash
    python client.py
    ```

## Dokumentasi

### Struktur Direktori

- `server.py`: Script untuk menjalankan server.
- `client.py`: Script untuk menjalankan client.

### Contoh Penggunaan

#### Menjalankan Server

Saat menjalankan server, akan ditampilkan log aktivitas server termasuk permintaan yang diterima dan diproses.

```bash
$ python server.py
* Running on http://127.0.0.1:8081/ (Press CTRL+C to quit)
```

#### Menjalankan Client

Client akan menampilkan antarmuka untuk melakukan berbagai fungsi seperti melihat daftar klinik yang buka, melakukan registrasi, dan booking antrian.

## Kontributor

Disusun oleh kelompok 7, kelas 3B 2021 Teknik Informatika, Jurusan Teknik Komputer dan Informatika, Politeknik Negeri Bandung.
- Azis Surohman
- Aini Diah Rahmawati
- Delvito Rahim Derivansyah
- Mentari Ayu Alysia Sudrajat


## Catatan

Untuk informasi lebih lanjut, silakan merujuk ke [[dokumentasi proyek](TB-Kelompok7.pdf)](https://drive.google.com/file/d/156TWqj4f1RMaDC7IHBZ7PYNlxGYJeT_Y/view?usp=sharing).
  
