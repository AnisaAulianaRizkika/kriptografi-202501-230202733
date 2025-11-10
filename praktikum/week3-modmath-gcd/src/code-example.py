# ==============================================
# Program: Kriptografi Dasar - Modular Arithmetic & GCD
# Fitur:
# 1. Operasi aritmetika modular
# 2. GCD dan Invers Modular (Algoritma Euclidean)
# 3. Identifikasi bilangan prima
# 4. Simulasi sederhana Logaritma Diskrit
# ==============================================

import random

# ======== Fungsi Dasar Aritmetika Modular ========

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

# ======== Fungsi Cek Bilangan Prima ========

def is_prime(n):
    """Pemeriksaan prima sederhana (cek hingga akar n)"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# ======== Simulasi Logaritma Diskrit (Brute Force) ========

def discrete_log(g, h, p):
    """
    Menyelesaikan g^x ≡ h (mod p)
    dengan metode brute force sederhana.
    """
    for x in range(p):
        if pow(g, x, p) == h:
            return x
    return None

# ======== Menu CLI ========

def menu():
    while True:
        print("\n=== MENU KRIPTOGRAFI DASAR ===")
        print("1. Operasi Aritmetika Modular")
        print("2. GCD & Invers Modular (Euclidean)")
        print("3. Cek Bilangan Prima")
        print("4. Simulasi Logaritma Diskrit")
        print("5. Keluar")

        pilih = input("Pilih menu (1-5): ")

        if pilih == "1":
            a = int(input("Masukkan a: "))
            b = int(input("Masukkan b: "))
            m = int(input("Masukkan modulus m: "))

            print(f"{a} + {b} mod {m} = {(a + b) % m}")
            print(f"{a} - {b} mod {m} = {(a - b) % m}")
            print(f"{a} × {b} mod {m} = {(a * b) % m}")
            print(f"{a}^{b} mod {m} = {pow(a, b, m)}")

        elif pilih == "2":
            a = int(input("Masukkan bilangan pertama: "))
            b = int(input("Masukkan bilangan kedua: "))
            print(f"GCD({a}, {b}) = {gcd(a, b)}")

            try:
                m = int(input("Masukkan modulus (untuk invers modular): "))
                inv = mod_inv(a, m)
                print(f"Invers modular dari {a} mod {m} = {inv}")
            except Exception as e:
                print(f"Error: {e}")

        elif pilih == "3":
            n = int(input("Masukkan bilangan yang ingin diuji: "))
            if is_prime(n):
                print(f"{n} adalah bilangan prima.")
            else:
                print(f"{n} bukan bilangan prima.")

        elif pilih == "4":
            p = int(input("Masukkan bilangan prima p: "))
            g = int(input("Masukkan basis (generator) g: "))
            x = random.randint(2, p - 2)
            h = pow(g, x, p)

            print(f"Nilai publik: h = g^x mod p = {h}")
            hasil = discrete_log(g, h, p)
            if hasil is not None:
                print(f"Ditemukan logaritma diskrit: x = {hasil}")
            else:
                print("Tidak ditemukan solusi logaritma diskrit.")

        elif pilih == "5":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

# ======== Jalankan Program ========
if __name__ == "__main__":
    menu()
