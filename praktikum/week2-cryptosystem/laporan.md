# Laporan Praktikum Kriptografi
Minggu ke-: 2
Topik: cryptosystem
Nama: Anisa Auliana Rizkika
NIM: 230202733 
Kelas: 5IKKA 

---

## 1. Tujuan
Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
Menggambarkan proses enkripsi dan dekripsi sederhana.
Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).

---

## 2. Dasar Teori
Cryptosystem adalah sistem yang digunakan untuk mengamankan komunikasi atau data dengan cara mengubah informasi asli (plaintext) menjadi bentuk yang tidak dapat dibaca (ciphertext) menggunakan algoritma dan kunci tertentu. Proses ini disebut enkripsi, sedangkan mengembalikan ciphertext ke bentuk semula disebut dekripsi.
Sebuah cryptosystem umumnya terdiri dari:
Algoritma enkripsi dan dekripsi – prosedur matematis untuk mengubah data.
Kunci (key) – nilai rahasia yang digunakan dalam proses enkripsi dan dekripsi.
Plaintext dan ciphertext – data asli dan hasil enkripsi.
Tujuan utama cryptosystem adalah menjaga kerahasiaan (confidentiality), integritas (integrity), dan autentikasi (authentication) dalam komunikasi digital.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
# --- Program utama ---
if __name__ == "__main__":
    print("=== Advanced Cryptosystem: Huruf + Angka Acak ===")
    text = input("Masukkan teks yang ingin dienkripsi: ")
    key = int(input("Masukkan kunci (angka bebas, misal 5): "))

    encrypted = encrypt(text, key)
    print(f"\nHasil Enkripsi : {encrypted}")

    decrypted = decrypt(encrypted, key)
    print(f"Hasil Dekripsi : {decrypted}")
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
1. Komponen utama kriptosistem:
Plaintext: pesan asli sebelum dienkripsi
Ciphertext: hasil enkripsi
Algoritma enkripsi & dekripsi: proses pengubahan data
Kunci (key): nilai rahasia untuk enkripsi dan dekripsi
2. Kelebihan & kelemahan sistem simetris dibandingkan asimetris:
Kelebihan: proses enkripsi dan dekripsi lebih cepat
Kelemahan: perlu berbagi kunci rahasia dengan aman (rawan bocor)
3. Distribusi kunci jadi masalah utama karena:
Dalam kriptografi simetris, pengirim dan penerima harus memiliki kunci yang sama, sehingga sulit mengirimkan kunci tersebut secara aman tanpa risiko disadap.
---

## 8. Kesimpulan
Cryptosystem merupakan sistem yang digunakan untuk menjaga keamanan data melalui proses enkripsi dan dekripsi dengan bantuan algoritma serta kunci tertentu. Tujuan utamanya adalah melindungi kerahasiaan, keaslian, dan integritas informasi dalam komunikasi digital. Dengan penerapan cryptosystem, data menjadi lebih aman dari akses atau penyadapan pihak yang tidak berwenang.

---

## 9. Daftar Pustaka
-Telkom University. Apa itu Kriptografi: Pengertian, Jenis, dan Manfaat. Diakses dari https://it.telkomuniversity.ac.id/kriptografi-adalah/
-BKI Academy. Kriptografi dalam Menjamin Keamanan Digital Informasi Publik. Diakses dari https://www.bki.academy/id/blog/travel-1/kriptografi-dalam-menjamin-keamanan-digital-informasi-publik-2
-IBM Indonesia. Jenis Kriptografi. Diakses dari https://www.ibm.com/id-id/think/topics/cryptography-types

---

## 10. Commit Log
```
commit anisa auliana rizkika 230202733
Author: Anisa Auliana Rizkika <riskikaanissa@gmail.com>
Date:   2025-11-04

    week2-cryptosystem: implementasi Caesar Cipher dan laporan 
```
