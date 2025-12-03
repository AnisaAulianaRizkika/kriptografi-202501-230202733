# Laporan Praktikum Kriptografi
Minggu ke-: 4  
Topik: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)  
Nama: Anisa Auliana Rizkika  
NIM: 230202733  
Kelas: 5IKKA  

---

## 1. Tujuan
- Menyelesaikan perhitungan sederhana terkait entropi kunci.
- Menggunakan teorema Euler pada contoh perhitungan modular & invers.
- Menghitung unicity distance untuk ciphertext tertentu.
- Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
- Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori
    Entropy adalah ukuran seberapa acak dan kuat sebuah kunci kriptografi. Semakin tinggi nilai entropy, semakin banyak kemungkinan kunci yang harus ditebak oleh penyerang, sehingga serangan brute force menjadi sangat sulit dan memakan waktu lama. Kunci dengan entropy tinggi berarti peluang menebaknya sangat kecil.
    
    Unicity Distance adalah jumlah minimum data terenkripsi (ciphertext) yang dibutuhkan agar penyerang bisa menentukan satu kunci yang benar melalui analisis. Semakin besar nilai unicity distance, semakin banyak ciphertext yang diperlukan untuk menemukan kunci, sehingga sistem lebih aman dari serangan berbasis analisis data.
    
    Keduanya digunakan untuk menilai kekuatan sistem kriptografi. Entropy tinggi membuat kunci sulit ditebak, sedangkan unicity distance tinggi membuat kunci sulit dipastikan dari ciphertext, sehingga secara umum keamanan terhadap serangan brute force menjadi lebih baik.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan
---

## 4. Langkah Percobaan
1. Perhitungan Entropi`.
2. Menghitung Unicity Distance
3. Analisis Brute Force

---

## 5. Source Code
def unicity_distance_bits(key_entropy_bits: float, redundancy_bits_per_char: float) -> float:
    if redundancy_bits_per_char <= 0:
        raise ValueError("redundancy_bits_per_char harus > 0")
    return key_entropy_bits / redundancy_bits_per_char

---

## 6. Hasil dan Pembahasan
Ringkasan hasil uji menunjukkan bahwa nilai unicity distance meningkat seiring bertambahnya entropy kunci dan menurun ketika redundansi pesan semakin besar. Pada kunci dengan entropy tinggi (misalnya 128–256 bit), dibutuhkan jumlah ciphertext yang jauh lebih banyak untuk dapat menentukan kunci secara unik, sedangkan pada kunci ber-entropy rendah atau pesan dengan redundansi tinggi, jumlah ciphertext yang diperlukan menjadi lebih sedikit. Hal ini membuktikan bahwa penggunaan kunci yang kuat serta pengurangan redundansi data sangat penting untuk meningkatkan ketahanan cipher terhadap serangan analisis dan brute force.

---

## 7. Jawaban Pertanyaan

- Pertanyaan 1: Apa arti dari nilai entropy dalam konteks kekuatan kunci?
Nilai entropy dalam konteks kekuatan kunci menunjukkan tingkat keacakan dan banyaknya kemungkinan kombinasi kunci yang tersedia; semakin besar entropy, semakin luas ruang pencarian yang harus dicoba penyerang, sehingga kunci menjadi lebih sulit ditebak dengan brute force dan lebih aman digunakan.
- Pertanyaan 2: Mengapa unicity distance penting dalam menentukan keamanan suatu cipher?
Unicity distance penting karena menunjukkan seberapa banyak ciphertext yang diperlukan agar sebuah kunci dapat ditentukan secara unik melalui analisis statistik; semakin besar unicity distance, semakin sulit bagi penyerang menemukan kunci yang benar meskipun memiliki data terenkripsi dalam jumlah besar, sehingga cipher menjadi lebih kuat terhadap serangan analisis dan lebih aman digunakan.
- Pertanyaan 3: Mengapa brute force masih menjadi ancaman meskipun algoritma sudah kuat?
Brute force masih menjadi ancaman karena kekuatan algoritma kriptografi tetap bergantung pada kualitas dan panjang kunci yang digunakan. Jika kunci memiliki entropy rendah—misalnya terlalu pendek, mudah ditebak, atau dibuat dari pola sederhana—penyerang masih bisa mencoba semua kemungkinan kunci satu per satu sampai menemukan yang benar. Selain itu, perkembangan daya komputasi dan penggunaan teknologi seperti komputasi paralel dan GPU juga membuat proses brute force semakin cepat, sehingga kunci yang dulu dianggap aman dapat menjadi rentan jika tidak diperbarui sesuai standar keamanan terbaru.

---

## 8. Kesimpulan
Berdasarkan percobaan, semakin tinggi nilai entropy kunci, semakin besar tingkat keamanan karena serangan brute force membutuhkan waktu yang jauh lebih lama. Nilai unicity distance yang besar juga menunjukkan bahwa lebih banyak ciphertext diperlukan untuk menemukan kunci, sehingga analisis menjadi semakin sulit. Kesimpulannya, keamanan cipher sangat dipengaruhi oleh kualitas kunci dan cukupnya data yang tersedia bagi penyerang.

---

## 9. Daftar Pustaka 
- Wibowo, E., & Kurniawan, D. (2020). Analisis Keamanan Data Menggunakan Algoritma Kriptografi terhadap Serangan Brute Force. Jurnal RESTI (Rekayasa Sistem dan Teknologi Informasi).  
- Nugraha, Y., & Puspitasari, N. (2021). Implementasi dan Evaluasi Keamanan Cipher Berbasis Kekuatan Kunci. Jurnal Informatika Universitas Pamulang
---

## 10. Commit Log

commit abc12345
Author: Anisa Auliana Rizkika <Riskikaanissa@gmail.com>
Date:   2025-12-03

    week4-entropy-unicity: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)
```
