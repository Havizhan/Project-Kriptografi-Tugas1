#!/usr/bin/env python3
"""
Demo penggunaan kriptosistem
"""

from ciphers import (
    ShiftCipher, SubstitutionCipher, AffineCipher,
    VigenereCipher, HillCipher, PermutationCipher
)

def demo_shift_cipher():
    print("=== Demo Shift Cipher ===")
    cipher = ShiftCipher(3)
    plaintext = "HELLO WORLD"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print()

def demo_substitution_cipher():
    print("=== Demo Substitution Cipher ===")
    key = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    cipher = SubstitutionCipher(key)
    plaintext = "HELLO WORLD"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print()

def demo_affine_cipher():
    print("=== Demo Affine Cipher ===")
    cipher = AffineCipher(5, 8)
    plaintext = "HELLO WORLD"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print()

def demo_vigenere_cipher():
    print("=== Demo Vigenere Cipher ===")
    cipher = VigenereCipher("KEYWORD")
    plaintext = "HELLO WORLD"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print()

def demo_hill_cipher():
    print("=== Demo Hill Cipher ===")
    cipher = HillCipher("GYBNQKURP")
    plaintext = "HELLO WORLD"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print()

def demo_permutation_cipher():
    print("=== Demo Permutation Cipher ===")
    cipher = PermutationCipher("2,0,1")
    plaintext = "HELLO WORLD"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print()

def demo_file_encryption():
    print("=== Demo File Encryption ===")
    cipher = ShiftCipher(5)
    
    # Simulasi data file
    test_data = b"This is a test file content!"
    print(f"Original data: {test_data}")
    
    # Enkripsi
    encrypted_data = cipher.encrypt_bytes(test_data)
    print(f"Encrypted data: {encrypted_data}")
    
    # Dekripsi
    decrypted_data = cipher.decrypt_bytes(encrypted_data)
    print(f"Decrypted data: {decrypted_data}")
    print()

if __name__ == "__main__":
    print("Demo Kriptosistem Sederhana")
    print("=" * 50)
    
    demo_shift_cipher()
    demo_substitution_cipher()
    demo_affine_cipher()
    demo_vigenere_cipher()
    demo_hill_cipher()
    demo_permutation_cipher()
    demo_file_encryption()
    
    print("Demo selesai!")
    print("\nUntuk menggunakan aplikasi web:")
    print("1. Jalankan: python app.py")
    print("2. Buka browser: http://localhost:5000")
    print("3. Pilih algoritma cipher dan masukkan kunci")
    print("4. Input teks atau upload file")
    print("5. Klik Enkripsi atau Dekripsi")
