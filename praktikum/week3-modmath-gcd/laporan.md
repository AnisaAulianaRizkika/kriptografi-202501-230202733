# Laporan Praktikum Kriptografi
Minggu ke-: 3  
Topik: [Modular Math]  
Nama: [Anisa Auliana Rizkika]  
NIM: [230202733]  
Kelas: [5IKKA]  

---

## 1. Tujuan
1. Menyelesaikan operasi aritmetika modular.
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Aritmetika modular adalah sistem perhitungan yang berfokus pada sisa hasil pembagian suatu bilangan dengan bilangantertentu. Konsep ini erat kaitannya dengan GCD atau FPB, yaitu nilai terbesar yang dapat membagi dua bilangan tanpa meninggalkan sisa. GCD digunakan untuk mengetahui apakah dua bilangan saling relatif prima, yang merupakan syarat penting dalam beberapa algoritma kriptografi. Selain itu, bilangan prima, yaitu bilangan yang hanya memiliki dua pembagi (1 dan dirinya sendiri), memiliki peran besar dalam keamanan sistem enkripsi karena sulitnya memfaktorkan bilangan besar menjadi bilangan-bilangan prima penyusunnya.

Logaritma diskrit merupakan kebalikan dari operasi perpangkatan dalam aritmetika modular, namun proses pencariannya sangat sulit dilakukan secara komputasi, terutama pada bilangan yang berukuran besar. Kesulitan inilah yang menjadikan logaritma diskrit dasar penting dalam keamanan berbagai algoritma kriptografi modern, seperti Diffie-Hellman dan ElGamal. Dengan demikian, konsep aritmetika modular, GCD, bilangan prima, dan logaritma diskrit saling berhubungan dan membentuk landasan utama dalam perancangan sistem keamanan digital masa kini.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

---

## 4. Langkah Percobaan

1. Tuliskan fungsi untuk menghitung operasi modular dasar.
2. Implementasikan fungsi GCD dengan algoritma Euclidean.
3. Tambahkan fungsi untuk mencari invers modular.
4. Simulasikan logaritma diskrit sederhana

---

## 5. Source Code
```
def gcd(a, b):
    """Menghitung GCD menggunakan algoritma Euclidean"""
    while b != 0:
        a, b = b, a % b
    return abs(a)
def extended_gcd(a, b):
    """Versi extended untuk mencari x, y sehingga ax + by = gcd(a,b)"""
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        return g, y1, x1 - (a // b) * y1
def mod_inv(a, m):
    """Mencari invers modular dari a (jika ada)"""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"Tidak ada invers modular untuk {a} mod {m}")
    return x % m
)
```
---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 
---

## 7. Jawaban Pertanyaan
- Pertanyaan 1: Aritmetika modular berperan sebagai dasar perhitungan dalam kriptografi modern karena digunakan untuk proses pembangkitan kunci, enkripsi, dan dekripsi. Sistem ini memungkinkan operasi bilangan dilakukan dalam ruang terbatas sehingga menghasilkan fungsi yang sulit dibalik, sehingga keamanan data dapat terjaga.
- Pertanyaan 2: Invers modular penting karena digunakan untuk menghitung kunci dekripsi dari kunci enkripsi. Dalam algoritma kunci publik seperti RSA, kunci publik dan kunci privat saling terkait melalui hubungan invers modulo. Tanpa invers modular, pesan yang telah dienkripsi tidak dapat dikembalikan ke bentuk aslinya secara aman.
- Pertanyaan 3: Tantangan utamanya adalah tingkat kesulitannya yang sangat tinggi secara komputasi. Untuk modulus yang besar, proses mencari nilai pangkat yang tepat membutuhkan waktu dan sumber daya yang sangat besar, sehingga tidak dapat diselesaikan dengan cepat oleh komputer biasa. Hal inilah yang membuat logaritma diskrit menjadi dasar keamanan pada banyak sistem kriptografi.
---

## 8. Kesimpulan
Secara keseluruhan, aritmetika modular, GCD, bilangan prima, dan logaritma diskrit menjadi dasar penting dalam kriptografi modern. Aritmetika modular digunakan sebagai kerangka perhitungan utama dalam proses enkripsi dan dekripsi, sementara bilangan prima dan GCD berperan dalam pembentukan kunci yang aman. Invers modular memungkinkan kunci publik dan kunci privat saling terhubung, seperti pada RSA. Adapun logaritma diskrit memberikan tingkat keamanan tinggi karena sulitnya menyelesaikannya untuk modulus besar. Dengan demikian, kekuatan sistem kriptografi banyak bergantung pada sifat matematis dari konsep-konsep tersebut.

---

## 9. Daftar Pustaka
  
- Fitriani, N., & Susanto, H. (2020). "Implementasi Algoritma RSA dalam Pengamanan Data." Jurnal Informatika, 7(2), 115-122. Tersedia di: https://ejournal.stmik-budidarma.ac.id/index.php/jurikom/article/view/2463.  
- Ramadhani, R., & Utami, R. (2019). "Analisis Kriptografi Kunci Publik Menggunakan Metode Diffie-Hellman." Jurnal Teknologi Informasi dan Komunikasi, 10(1), 45-52. Tersedia di: https://jurnal.uisu.ac.id/index.php/jtik/article/view/1746

---

## 10. Commit Log

commit week3-modmath-gcd: Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)
Author: Anisa Auliana Rizkika <riskikaanissa@gmail.com>
Date:   2025-11-10

```
