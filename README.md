# Kriptosistem Sederhana

Implementasi berbagai algoritma kriptografi klasik dengan antarmuka web menggunakan Python Flask.

## Fitur

Aplikasi ini mengimplementasikan 6 algoritma kriptografi klasik:

1. **Shift Cipher (Caesar Cipher)** - Menggeser setiap huruf sejumlah posisi tertentu
2. **Substitution Cipher** - Mengganti setiap huruf dengan huruf lain berdasarkan tabel substitusi
3. **Affine Cipher** - Menggunakan fungsi matematika E(x) = (ax + b) mod 26
4. **Vigenere Cipher** - Menggunakan kunci berulang untuk enkripsi
5. **Hill Cipher** - Menggunakan matriks untuk enkripsi blok huruf
6. **Permutation Cipher** - Mengatur ulang posisi huruf dalam blok

### Fitur Tambahan:
- ✅ **Antarmuka Modern**: Desain responsif dengan Bootstrap 5
- ✅ **Drag & Drop**: Upload file dengan drag and drop
- ✅ **Format Output**: Tanpa spasi atau kelompok 5-huruf
- ✅ **Copy to Clipboard**: Salin hasil ke clipboard
- ✅ **Clear All**: Bersihkan semua input dengan satu klik
- ✅ **Dark Mode**: Dukungan mode gelap otomatis
- ✅ **File Validation**: Validasi ukuran dan tipe file
- ✅ **Error Handling**: Pesan error yang informatif
- ✅ **Loading Indicators**: Indikator loading yang smooth

## Spesifikasi

- ✅ Enkripsi dan dekripsi teks
- ✅ Enkripsi dan dekripsi file (semua jenis file)
- ✅ Antarmuka web yang user-friendly
- ✅ Format output: tanpa spasi atau kelompok 5-huruf
- ✅ Download file hasil enkripsi/dekripsi
- ✅ Validasi kunci untuk setiap algoritma
- ✅ Dukungan file hingga 16MB

## Instalasi

1. Clone atau download repository ini
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi:
```bash
python app.py
```

4. Buka browser dan akses: `http://localhost:5000`

## Cara Penggunaan

### 1. Shift Cipher
- **Kunci**: Angka 0-25 (contoh: 3)
- **Cara kerja**: Menggeser setiap huruf sejumlah posisi dalam alfabet

### 2. Substitution Cipher
- **Kunci**: 26 huruf unik (contoh: ZYXWVUTSRQPONMLKJIHGFEDCBA)
- **Cara kerja**: Mengganti setiap huruf dengan huruf lain berdasarkan tabel

### 3. Affine Cipher
- **Kunci**: Dua angka dipisahkan koma (contoh: 5,8)
- **Cara kerja**: Menggunakan fungsi E(x) = (ax + b) mod 26
- **Catatan**: Angka pertama (a) harus coprime dengan 26

### 4. Vigenere Cipher
- **Kunci**: Kata kunci (contoh: KEYWORD)
- **Cara kerja**: Menggunakan kunci berulang untuk enkripsi

### 5. Hill Cipher
- **Kunci**: String yang akan dikonversi menjadi matriks (contoh: GYBNQKURP)
- **Cara kerja**: Menggunakan matriks untuk enkripsi blok huruf
- **Catatan**: Panjang kunci harus perfect square (4, 9, 16, dst.)

### 6. Permutation Cipher
- **Kunci**: Urutan posisi dipisahkan koma (contoh: 2,0,1)
- **Cara kerja**: Mengatur ulang posisi huruf dalam blok

## Struktur File

```
kriptosystem/
├── app.py              # Aplikasi Flask utama
├── ciphers.py          # Implementasi semua algoritma cipher
├── requirements.txt    # Dependencies Python
├── README.md          # Dokumentasi
├── demo.py            # Demo penggunaan cipher
├── test_ciphers.py    # Test semua cipher
├── generate_otp_key.py # Generator kunci One-Time Pad
├── templates/
│   └── index.html     # Antarmuka web HTML
└── static/            # File statis
    ├── css/
    │   └── style.css  # Styling CSS
    └── js/
        └── app.js     # JavaScript aplikasi
```

## Teknologi yang Digunakan

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Matematika**: NumPy untuk operasi matriks (Hill Cipher)
- **Icons**: Font Awesome

## Catatan Penting

1. **File Enkripsi**: File yang dienkripsi akan disimpan dengan ekstensi `.dat`
2. **Dekripsi File**: Pastikan menggunakan kunci yang sama untuk mendekripsi
3. **Format File**: File hasil dekripsi harus disimpan dengan ekstensi asli agar bisa dibuka
4. **Karakter Non-Alfabet**: Untuk Vigenere, Hill, dan Permutation cipher, karakter non-alfabet akan diabaikan
5. **Ukuran File**: Maksimal 16MB per file

## Contoh Penggunaan

### Enkripsi Teks
1. Pilih algoritma cipher
2. Masukkan kunci sesuai format
3. Ketik teks di area input
4. Klik "Enkripsi"
5. Hasil akan ditampilkan di bawah

### Enkripsi File
1. Pilih algoritma cipher
2. Masukkan kunci sesuai format
3. Pilih mode "Upload File"
4. Upload file yang akan dienkripsi
5. Klik "Enkripsi"
6. Download file hasil enkripsi

## Lisensi

Project ini dibuat untuk keperluan akademik mata kuliah Kriptografi.

## Kontributor

Dibuat untuk memenuhi tugas mata kuliah Kriptografi Semester 5.
