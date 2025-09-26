#!/usr/bin/env python3
"""
Script untuk testing semua cipher
"""

from ciphers import (
    ShiftCipher, SubstitutionCipher, AffineCipher,
    VigenereCipher, HillCipher, PermutationCipher
)

def test_shift_cipher():
    print("=== Testing Shift Cipher ===")
    cipher = ShiftCipher(3)
    plaintext = "HELLO WORLD"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Success: {plaintext == decrypted}")
    print()

def test_substitution_cipher():
    print("=== Testing Substitution Cipher ===")
    key = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    cipher = SubstitutionCipher(key)
    plaintext = "HELLO WORLD"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Success: {plaintext == decrypted}")
    print()

def test_affine_cipher():
    print("=== Testing Affine Cipher ===")
    cipher = AffineCipher(5, 8)
    plaintext = "HELLO WORLD"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Success: {plaintext == decrypted}")
    print()

def test_vigenere_cipher():
    print("=== Testing Vigenere Cipher ===")
    cipher = VigenereCipher("KEYWORD")
    plaintext = "HELLO WORLD"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Success: {plaintext == decrypted}")
    print()

def test_hill_cipher():
    print("=== Testing Hill Cipher ===")
    cipher = HillCipher("GYBNQKURP")
    plaintext = "HELLO WORLD"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Success: {plaintext == decrypted}")
    print()

def test_permutation_cipher():
    print("=== Testing Permutation Cipher ===")
    cipher = PermutationCipher("2,0,1")
    plaintext = "HELLO WORLD"
    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Success: {plaintext == decrypted}")
    print()

def test_file_encryption():
    print("=== Testing File Encryption ===")
    # Test dengan Shift Cipher
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
    print(f"Success: {test_data == decrypted_data}")
    print()

if __name__ == "__main__":
    print("Testing All Ciphers")
    print("=" * 50)
    
    test_shift_cipher()
    test_substitution_cipher()
    test_affine_cipher()
    test_vigenere_cipher()
    test_hill_cipher()
    test_permutation_cipher()
    test_file_encryption()
    
    print("All tests completed!")
