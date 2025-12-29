# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi)  
Nama: Anisa Auliana Rizkika  
NIM: 230202733 
Kelas: 5IKKA 

---

## 1. Tujuan
1. Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
2. Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
3. Mengimplementasikan algoritma transposisi sederhana.
4. Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori
Cipher klasik merupakan metode kriptografi awal yang digunakan untuk menjaga kerahasiaan pesan dengan cara menyamarkan teks asli (plaintext) menjadi teks tersandi (ciphertext). Teknik ini bekerja menggunakan prinsip sederhana, seperti pergeseran huruf, penggunaan kata kunci, atau pengaturan ulang posisi karakter. Meskipun mekanismenya masih manual dan sederhana, cipher klasik menjadi fondasi penting dalam perkembangan ilmu kriptografi dan keamanan informasi.
Caesar Cipher dan Vigenère Cipher termasuk dalam kategori substitusi, yaitu metode yang mengganti huruf plaintext dengan huruf lain berdasarkan aturan tertentu. Caesar Cipher menggunakan satu nilai pergeseran tetap sehingga mudah dianalisis, sedangkan Vigenère Cipher memakai kata kunci untuk menghasilkan pergeseran yang bervariasi, sehingga relatif lebih aman dibanding Caesar. Namun, keduanya tetap rentan terhadap analisis frekuensi, terutama jika kunci yang digunakan pendek atau berulang.
Berbeda dengan substitusi, Transposisi Cipher tidak mengubah karakter, melainkan hanya mengacak urutan huruf dalam pesan berdasarkan pola tertentu. Metode ini menjaga frekuensi huruf tetap sama, tetapi menyulitkan pembacaan pesan tanpa mengetahui pola pengacakan. Walaupun cipher klasik saat ini sudah tidak digunakan untuk pengamanan data modern, konsepnya tetap relevan sebagai dasar pembelajaran untuk memahami cara kerja enkripsi sebelum berkembang ke algoritma kriptografi modern.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
1. Implementasi Caesar Cipher
2. Implementasi Vigenère Cipher
3. Implementasi Transposisi Sederhana

---

## 5. Source Code

# contoh potongan kode
def encrypt(text, key):
    return ...
```

---

## 6. Hasil dan Pembahasan

---

## 7. Jawaban Pertanyaan
- Pertanyaan 1: Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher?
Kelemahan utama Caesar Cipher adalah ruang kunci yang sangat kecil karena hanya menggunakan satu nilai pergeseran tetap, sehingga mudah dipecahkan dengan brute force atau mencoba semua kemungkinan pergeseran. Selain itu, pola frekuensi huruf pada plaintext tetap terlihat pada ciphertext sehingga mudah dianalisis.
Sementara itu, Vigenère Cipher memiliki kelemahan pada penggunaan kata kunci yang berulang. Jika panjang kunci dapat ditebak atau diketahui, ciphertext dapat dipecah menjadi beberapa Caesar Cipher terpisah. Dengan teknik seperti Kasiski Examination atau Friedman Test, Vigenère Cipher masih dapat dipecahkan menggunakan analisis statistik.

- Pertanyaan 2: Mengapa cipher klasik mudah diserang dengan analisis frekuensi?
Cipher klasik umumnya tidak menyembunyikan pola statistik bahasa alami. Huruf-huruf tertentu seperti vokal atau konsonan umum tetap muncul dengan frekuensi yang sama, meskipun bentuknya telah disamarkan. Karena distribusi frekuensi huruf dalam suatu bahasa relatif konsisten, penyerang dapat mencocokkan pola tersebut untuk menebak huruf asli. Semakin panjang pesan dan semakin sederhana algoritmanya, semakin mudah pola ini dikenali.

- Pertanyaan 3: Perbandingan cipher substitusi dan transposisi
Cipher Substitusi mengganti setiap karakter plaintext dengan karakter lain berdasarkan aturan tertentu. Kelebihannya adalah proses enkripsi yang sederhana dan cepat, namun kelemahannya terletak pada pola frekuensi huruf yang masih dapat dikenali, sehingga rentan terhadap analisis frekuensi.
Cipher Transposisi hanya mengubah urutan karakter tanpa mengganti hurufnya. Kelebihannya adalah tidak mengubah frekuensi huruf sehingga menyulitkan analisis substitusi langsung, tetapi kelemahannya adalah pola susunan teks masih bisa dipecahkan jika aturan pengacakan diketahui. Secara umum, kedua metode lebih aman jika dikombinasikan, namun secara terpisah masih lemah untuk standar keamanan modern.

---

## 8. Kesimpulan
Cipher klasik seperti Caesar, Vigenère, dan Transposisi memiliki peran penting dalam sejarah kriptografi sebagai dasar pengembangan teknik enkripsi. Namun, keterbatasan utama cipher ini terletak pada mekanisme pengamanan yang sederhana dan masih mempertahankan pola statistik bahasa, sehingga mudah diserang menggunakan brute force maupun analisis frekuensi.
Perbandingan antara cipher substitusi dan transposisi menunjukkan bahwa masing-masing memiliki kelebihan dan kelemahan, tetapi keduanya belum mampu memberikan tingkat keamanan yang memadai jika digunakan secara terpisah. Oleh karena itu, cipher klasik saat ini lebih relevan sebagai media pembelajaran konsep kriptografi, sementara kebutuhan keamanan modern menuntut algoritma yang lebih kompleks dan kuat.

---

## 9. Daftar Pustaka
Kurniawan, A., & Prasetyo, E. (2017). “Analisis Algoritma Kriptografi Klasik Caesar Cipher dan Vigenère Cipher.” Jurnal Teknologi Informasi dan Ilmu Komputer, 4(2), 85–92.

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit week5-cipher-klasik
Author: Anisa Auliana Rizkika <riskikaanissa@gmail.com>
Date:   2025-12-29

    week5-cryptosystem: Cipher Klasik (Caesar, Vigenère, Transposisi)
```
