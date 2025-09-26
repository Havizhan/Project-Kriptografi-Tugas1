#!/usr/bin/env python3
"""
Script untuk generate kunci One-Time Pad
Membuat file berisi huruf-huruf acak untuk digunakan sebagai kunci OTP
"""

import random
import string

def generate_otp_key(length=10000, filename="otp_key.txt"):
    """
    Generate kunci One-Time Pad dengan huruf acak
    
    Args:
        length (int): Panjang kunci yang diinginkan
        filename (str): Nama file untuk menyimpan kunci
    """
    # Generate huruf acak
    key = ''.join(random.choices(string.ascii_uppercase, k=length))
    
    # Simpan ke file
    with open(filename, 'w') as f:
        f.write(key)
    
    print(f"Kunci OTP berhasil dibuat!")
    print(f"Panjang: {length} karakter")
    print(f"File: {filename}")
    print(f"Contoh kunci: {key[:50]}...")

if __name__ == "__main__":
    # Generate kunci dengan panjang 10000 karakter
    generate_otp_key(10000, "otp_key.txt")
    
    # Generate kunci dengan panjang 50000 karakter
    generate_otp_key(50000, "otp_key_large.txt")
