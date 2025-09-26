import re
import numpy as np
from typing import List, Union
import random
import string

class BaseCipher:
    """Base class untuk semua cipher"""
    
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    
    def clean_text(self, text: str, keep_spaces: bool = False) -> str:
        """Membersihkan teks, hanya menyisakan huruf alfabet"""
        if keep_spaces:
            return re.sub(r'[^A-Za-z\s]', '', text.upper())
        return re.sub(r'[^A-Za-z]', '', text.upper())
    
    def preserve_spaces(self, original: str, processed: str) -> str:
        """Mempertahankan posisi spasi dalam teks yang sudah diproses"""
        result = []
        processed_idx = 0
        
        for char in original:
            if char.isalpha():
                if processed_idx < len(processed):
                    result.append(processed[processed_idx])
                    processed_idx += 1
                else:
                    result.append(char)
            else:
                result.append(char)
        
        return ''.join(result)
    
    def encrypt_bytes(self, data: bytes) -> bytes:
        """Enkripsi data bytes"""
        # Konversi bytes ke list of integers
        byte_list = list(data)
        encrypted_bytes = []
        
        for byte_val in byte_list:
            # Enkripsi setiap byte sebagai karakter
            char = chr(byte_val)
            encrypted_char = self.encrypt(char)
            # Ambil karakter pertama jika hasil enkripsi lebih dari 1 karakter
            if len(encrypted_char) > 0:
                encrypted_bytes.append(ord(encrypted_char[0]) % 256)
            else:
                encrypted_bytes.append(byte_val)
        
        return bytes(encrypted_bytes)
    
    def decrypt_bytes(self, data: bytes) -> bytes:
        """Dekripsi data bytes"""
        # Konversi bytes ke list of integers
        byte_list = list(data)
        decrypted_bytes = []
        
        for byte_val in byte_list:
            # Dekripsi setiap byte sebagai karakter
            char = chr(byte_val)
            decrypted_char = self.decrypt(char)
            # Ambil karakter pertama jika hasil dekripsi lebih dari 1 karakter
            if len(decrypted_char) > 0:
                decrypted_bytes.append(ord(decrypted_char[0]) % 256)
            else:
                decrypted_bytes.append(byte_val)
        
        return bytes(decrypted_bytes)

class ShiftCipher(BaseCipher):
    """Implementasi Shift Cipher (Caesar Cipher)"""
    
    def __init__(self, shift: int = 3):
        super().__init__()
        self.shift = shift % 26
    
    def encrypt(self, text: str) -> str:
        """Enkripsi teks menggunakan shift cipher"""
        result = []
        
        for char in text.upper():
            if char.isalpha():
                # Konversi ke indeks (0-25)
                char_index = ord(char) - ord('A')
                # Shift dan wrap around
                new_index = (char_index + self.shift) % 26
                result.append(chr(new_index + ord('A')))
            else:
                result.append(char)
        
        return ''.join(result)
    
    def decrypt(self, text: str) -> str:
        """Dekripsi teks menggunakan shift cipher"""
        result = []
        
        for char in text.upper():
            if char.isalpha():
                # Konversi ke indeks (0-25)
                char_index = ord(char) - ord('A')
                # Shift mundur dan wrap around
                new_index = (char_index - self.shift) % 26
                result.append(chr(new_index + ord('A')))
            else:
                result.append(char)
        
        return ''.join(result)

class SubstitutionCipher(BaseCipher):
    """Implementasi Substitution Cipher"""
    
    def __init__(self, key: str = ""):
        super().__init__()
        if key:
            self.key = self.clean_text(key)
        else:
            # Generate random key jika tidak ada
            self.key = ''.join(random.sample(self.alphabet, 26))
        
        # Buat mapping untuk enkripsi dan dekripsi
        self.encrypt_map = {self.alphabet[i]: self.key[i] for i in range(26)}
        self.decrypt_map = {self.key[i]: self.alphabet[i] for i in range(26)}
    
    def encrypt(self, text: str) -> str:
        """Enkripsi teks menggunakan substitution cipher"""
        result = []
        
        for char in text.upper():
            if char.isalpha():
                result.append(self.encrypt_map.get(char, char))
            else:
                result.append(char)
        
        return ''.join(result)
    
    def decrypt(self, text: str) -> str:
        """Dekripsi teks menggunakan substitution cipher"""
        result = []
        
        for char in text.upper():
            if char.isalpha():
                result.append(self.decrypt_map.get(char, char))
            else:
                result.append(char)
        
        return ''.join(result)

class AffineCipher(BaseCipher):
    """Implementasi Affine Cipher"""
    
    def __init__(self, a: int = 1, b: int = 0):
        super().__init__()
        self.a = a % 26
        self.b = b % 26
        
        # Validasi bahwa gcd(a, 26) = 1
        if self.gcd(self.a, 26) != 1:
            raise ValueError("a dan 26 harus coprime (gcd(a, 26) = 1)")
        
        # Hitung modular inverse dari a
        self.a_inv = self.mod_inverse(self.a, 26)
    
    def gcd(self, a: int, b: int) -> int:
        """Menghitung Greatest Common Divisor"""
        while b:
            a, b = b, a % b
        return a
    
    def mod_inverse(self, a: int, m: int) -> int:
        """Menghitung modular inverse"""
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return 1
    
    def encrypt(self, text: str) -> str:
        """Enkripsi teks menggunakan affine cipher"""
        result = []
        
        for char in text.upper():
            if char.isalpha():
                char_index = ord(char) - ord('A')
                new_index = (self.a * char_index + self.b) % 26
                result.append(chr(new_index + ord('A')))
            else:
                result.append(char)
        
        return ''.join(result)
    
    def decrypt(self, text: str) -> str:
        """Dekripsi teks menggunakan affine cipher"""
        result = []
        
        for char in text.upper():
            if char.isalpha():
                char_index = ord(char) - ord('A')
                new_index = (self.a_inv * (char_index - self.b)) % 26
                result.append(chr(new_index + ord('A')))
            else:
                result.append(char)
        
        return ''.join(result)

class VigenereCipher(BaseCipher):
    """Implementasi Vigenere Cipher"""
    
    def __init__(self, key: str = ""):
        super().__init__()
        self.key = self.clean_text(key)
        if not self.key:
            self.key = "KEY"
    
    def encrypt(self, text: str) -> str:
        """Enkripsi teks menggunakan vigenere cipher"""
        result = []
        key_index = 0
        
        for char in text.upper():
            if char.isalpha():
                char_index = ord(char) - ord('A')
                key_char_index = ord(self.key[key_index % len(self.key)]) - ord('A')
                new_index = (char_index + key_char_index) % 26
                result.append(chr(new_index + ord('A')))
                key_index += 1
            else:
                result.append(char)
        
        return ''.join(result)
    
    def decrypt(self, text: str) -> str:
        """Dekripsi teks menggunakan vigenere cipher"""
        result = []
        key_index = 0
        
        for char in text.upper():
            if char.isalpha():
                char_index = ord(char) - ord('A')
                key_char_index = ord(self.key[key_index % len(self.key)]) - ord('A')
                new_index = (char_index - key_char_index) % 26
                result.append(chr(new_index + ord('A')))
                key_index += 1
            else:
                result.append(char)
        
        return ''.join(result)

class HillCipher(BaseCipher):
    """Implementasi Hill Cipher"""
    
    def __init__(self, key: str = ""):
        super().__init__()
        self.key_matrix = self.parse_key(key)
        self.key_matrix_inv = self.calculate_inverse(self.key_matrix)
    
    def parse_key(self, key: str) -> np.ndarray:
        """Parse key string menjadi matrix"""
        cleaned_key = self.clean_text(key)
        
        # Jika key kosong, gunakan key default
        if not cleaned_key:
            cleaned_key = "GYBNQKURP"
        
        # Pastikan panjang key adalah perfect square
        key_len = len(cleaned_key)
        matrix_size = int(key_len ** 0.5)
        
        if matrix_size * matrix_size != key_len:
            # Pad dengan 'A' jika perlu
            while matrix_size * matrix_size < key_len:
                matrix_size += 1
            cleaned_key += 'A' * (matrix_size * matrix_size - key_len)
            matrix_size = int(len(cleaned_key) ** 0.5)
        
        # Konversi ke matrix
        matrix = np.zeros((matrix_size, matrix_size), dtype=int)
        for i in range(matrix_size):
            for j in range(matrix_size):
                matrix[i][j] = ord(cleaned_key[i * matrix_size + j]) - ord('A')
        
        return matrix
    
    def calculate_inverse(self, matrix: np.ndarray) -> np.ndarray:
        """Hitung inverse matrix modulo 26"""
        det = int(round(np.linalg.det(matrix))) % 26
        
        # Hitung modular inverse dari determinant
        det_inv = self.mod_inverse(det, 26)
        
        # Hitung adjugate matrix
        adj = np.round(np.linalg.inv(matrix) * np.linalg.det(matrix)).astype(int) % 26
        
        # Hitung inverse matrix
        matrix_inv = (det_inv * adj) % 26
        
        return matrix_inv
    
    def mod_inverse(self, a: int, m: int) -> int:
        """Hitung modular inverse"""
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return 1
    
    def encrypt(self, text: str) -> str:
        """Enkripsi teks menggunakan hill cipher"""
        result = []
        matrix_size = self.key_matrix.shape[0]
        alpha_chars = []
        
        # Kumpulkan semua karakter alfabet
        for char in text.upper():
            if char.isalpha():
                alpha_chars.append(char)
        
        if not alpha_chars:
            return text
        
        # Pad text jika panjang tidak kelipatan matrix_size
        while len(alpha_chars) % matrix_size != 0:
            alpha_chars.append('X')
        
        # Enkripsi setiap blok
        for i in range(0, len(alpha_chars), matrix_size):
            block = alpha_chars[i:i + matrix_size]
            block_vector = np.array([ord(c) - ord('A') for c in block])
            
            # Enkripsi block
            encrypted_vector = np.dot(self.key_matrix, block_vector) % 26
            
            # Konversi kembali ke string
            for val in encrypted_vector:
                result.append(chr(int(val) + ord('A')))
        
        # Reconstruct dengan mempertahankan posisi karakter non-alfabet
        final_result = list(text.upper())
        alpha_idx = 0
        
        for i, char in enumerate(final_result):
            if char.isalpha():
                if alpha_idx < len(result):
                    final_result[i] = result[alpha_idx]
                    alpha_idx += 1
        
        return ''.join(final_result)
    
    def decrypt(self, text: str) -> str:
        """Dekripsi teks menggunakan hill cipher"""
        # Hanya proses karakter alfabet, abaikan yang lain
        alpha_chars = []
        
        for char in text.upper():
            if char.isalpha():
                alpha_chars.append(char)
        
        if not alpha_chars:
            return text
        
        matrix_size = self.key_matrix_inv.shape[0]
        
        # Pad text jika panjang tidak kelipatan matrix_size
        while len(alpha_chars) % matrix_size != 0:
            alpha_chars.append('X')
        
        result = []
        
        for i in range(0, len(alpha_chars), matrix_size):
            block = alpha_chars[i:i + matrix_size]
            block_vector = np.array([ord(c) - ord('A') for c in block])
            
            # Dekripsi block
            decrypted_vector = np.dot(self.key_matrix_inv, block_vector) % 26
            
            # Konversi kembali ke string
            for val in decrypted_vector:
                result.append(chr(int(val) + ord('A')))
        
        # Reconstruct dengan mempertahankan posisi karakter non-alfabet
        final_result = list(text.upper())
        alpha_idx = 0
        
        # Hitung jumlah karakter alfabet asli
        original_alpha_count = sum(1 for c in text.upper() if c.isalpha())
        
        for i, char in enumerate(final_result):
            if char.isalpha():
                if alpha_idx < original_alpha_count and alpha_idx < len(result):
                    final_result[i] = result[alpha_idx]
                    alpha_idx += 1
        
        return ''.join(final_result)

class PermutationCipher(BaseCipher):
    """Implementasi Permutation Cipher"""
    
    def __init__(self, key: str = ""):
        super().__init__()
        self.permutation = self.parse_permutation(key)
        self.inverse_permutation = self.calculate_inverse_permutation(self.permutation)
    
    def parse_permutation(self, key: str) -> List[int]:
        """Parse key string menjadi permutation"""
        if not key:
            # Default permutation: [2, 0, 1] untuk block size 3
            return [2, 0, 1]
        
        # Parse key sebagai angka yang dipisahkan koma atau spasi
        try:
            if ',' in key:
                permutation = [int(x.strip()) for x in key.split(',')]
            else:
                permutation = [int(x) for x in key.split()]
        except ValueError:
            # Jika gagal parse, gunakan default
            return [2, 0, 1]
        
        # Validasi permutation
        n = len(permutation)
        if sorted(permutation) != list(range(n)):
            return [2, 0, 1]  # Default jika tidak valid
        
        return permutation
    
    def calculate_inverse_permutation(self, permutation: List[int]) -> List[int]:
        """Hitung inverse permutation"""
        n = len(permutation)
        inverse = [0] * n
        for i in range(n):
            inverse[permutation[i]] = i
        return inverse
    
    def encrypt(self, text: str) -> str:
        """Enkripsi teks menggunakan permutation cipher"""
        # Hanya proses karakter alfabet, abaikan yang lain
        alpha_chars = []
        
        for char in text.upper():
            if char.isalpha():
                alpha_chars.append(char)
        
        if not alpha_chars:
            return text
        
        block_size = len(self.permutation)
        
        # Pad text jika panjang tidak kelipatan block_size
        while len(alpha_chars) % block_size != 0:
            alpha_chars.append('X')
        
        result = []
        
        for i in range(0, len(alpha_chars), block_size):
            block = alpha_chars[i:i + block_size]
            
            # Apply permutation
            permuted_block = [''] * block_size
            for j in range(block_size):
                permuted_block[self.permutation[j]] = block[j]
            
            result.extend(permuted_block)
        
        # Reconstruct dengan mempertahankan posisi karakter non-alfabet
        final_result = list(text.upper())
        alpha_idx = 0
        
        for i, char in enumerate(final_result):
            if char.isalpha():
                if alpha_idx < len(result):
                    final_result[i] = result[alpha_idx]
                    alpha_idx += 1
        
        return ''.join(final_result)
    
    def decrypt(self, text: str) -> str:
        """Dekripsi teks menggunakan permutation cipher"""
        # Hanya proses karakter alfabet, abaikan yang lain
        alpha_chars = []
        
        for char in text.upper():
            if char.isalpha():
                alpha_chars.append(char)
        
        if not alpha_chars:
            return text
        
        block_size = len(self.inverse_permutation)
        
        # Pad text jika panjang tidak kelipatan block_size
        while len(alpha_chars) % block_size != 0:
            alpha_chars.append('X')
        
        result = []
        
        for i in range(0, len(alpha_chars), block_size):
            block = alpha_chars[i:i + block_size]
            
            # Apply inverse permutation
            original_block = [''] * block_size
            for j in range(block_size):
                original_block[self.inverse_permutation[j]] = block[j]
            
            result.extend(original_block)
        
        # Reconstruct dengan mempertahankan posisi karakter non-alfabet
        final_result = list(text.upper())
        alpha_idx = 0
        
        # Hitung jumlah karakter alfabet asli
        original_alpha_count = sum(1 for c in text.upper() if c.isalpha())
        
        for i, char in enumerate(final_result):
            if char.isalpha():
                if alpha_idx < original_alpha_count and alpha_idx < len(result):
                    final_result[i] = result[alpha_idx]
                    alpha_idx += 1
        
        return ''.join(final_result)
