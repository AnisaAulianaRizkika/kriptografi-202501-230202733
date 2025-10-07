# Laporan Praktikum Kriptografi
Minggu ke-: 1
Topik: Sejarah Kriptografi & Prinsip CIA 
Nama: Anisa Auliana Rizkika  
NIM: 230202733  
Kelas: 5IKKA

---

## 1. Tujuan
1. Menjelaskan sejarah dan evolusi kriptografi dari masa klasik hingga modern.
2. Menyebutkan prinsip Confidentiality, Integrity, Availability (CIA) dengan benar.
3. Menyimpulkan peran kriptografi dalam sistem keamanan informasi modern.
4. Menyiapkan repositori GitHub sebagai media kerja praktikum

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(.  
- Pertanyaan 1: Siapa tokoh yang dianggap sebagai bapak kriptografi modern?
                  Tokoh yang dikenal sebagai bapak kriptografi modern adalah Claude E. Shannon yang pada tahun 1949 menerbitkan makalah berjudul “Communication Theory of Secrecy Systems”.
  
- Pertanyaan 2: Sebutkan algoritma kunci publik yang populer digunakan saat ini.
                  Beberapa algoritma kunci publik yang populer digunakan dalam kriptografi modern antara lain RSA (Rivest–Shamir–Adleman), Elliptic Curve Cryptography (ECC), Diffie–Hellman (DH), dan ElGamal. Algoritma RSA adalah yang paling terkenal dan sering digunakan untuk enkripsi data serta tanda tangan digital. ECC menawarkan keamanan tinggi dengan ukuran kunci yang lebih kecil, sehingga lebih efisien. Sementara itu, Diffie–Hellman digunakan untuk pertukaran kunci secara aman di jaringan, dan ElGamal banyak dipakai dalam sistem tanda tangan digital seperti Digital Signature Algorithm (DSA).
  
- Pertanyaan 3: Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
                  Perbedaan utama antara kriptografi klasik dan modern terletak pada cara kerja, jenis kunci, dan dasar keamanannya. Kriptografi klasik menggunakan satu kunci yang sama (simetris) untuk enkripsi dan dekripsi, serta bekerja pada huruf atau teks dengan metode seperti Caesar Cipher dan Vigenère Cipher. Keamanannya bergantung pada kerahasiaan algoritma yang digunakan. Sebaliknya, kriptografi modern menggunakan dua kunci berbeda, yaitu kunci publik dan kunci privat (asimetris), dan bekerja pada bit atau blok data digital. Keamanannya didasarkan pada kerahasiaan kunci, bukan algoritmanya, dengan contoh algoritma seperti AES, RSA, dan ECC.
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
