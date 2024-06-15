# SI-UKKW-SIWP2005_OOP_2024 Object-Oriented Programming

## HW#3: Build Your Own Python Package

### Overview
Dalam tugas ini, Anda akan membuat, membangun, dan mempublikasikan paket Python ke PyPi. Paket yang Anda kembangkan adalah koleksi algoritma pengurutan yang dapat digunakan untuk mengurutkan daftar angka. Paket ini akan mencakup beberapa algoritma pengurutan umum seperti bubble sort, insertion sort, dan quick sort. Anda akan mengikuti praktik terbaik untuk menyusun paket Anda, menulis dokumentasi, dan mempublikasikannya di PyPi.

### Objectives
- Memahami struktur paket Python.
- Menulis file setup.py untuk menentukan detail paket.
- Membuat file README.md dengan instruksi penggunaan.
- Mendaftarkan akun di PyPi.
- Membangun paket menggunakan setuptools dan wheel.
- Mengupload paket ke PyPi menggunakan twine.
- Memverifikasi paket di PyPi.

### Evaluation Criteria
- Struktur paket Python yang benar.
- Kelengkapan dan kebenaran setup.py dan README.md.
- Keberhasilan registrasi dan upload ke PyPi.
- Kode algoritma pengurutan yang jelas dan terdokumentasi dengan baik.
- Verifikasi fungsionalitas paket di PyPi.

### Project Structure
siwp2005-nayla-sort/
│
├── CHANGES.txt
├── LICENSE
├── MANIFEST.in
├── pyproject.toml
├── README.md
├── setup.cfg
├── setup.py
├── src/
│ └── sort/
│ ├── bubble_sort.py
│ ├── init.py
│ ├── insertion_sort.py
│ └── quick_sort.py
└── tests/
├── init.py
├── test_bubble_sort.py
├── test_insertion_sort.py
└── test_quick_sort.py