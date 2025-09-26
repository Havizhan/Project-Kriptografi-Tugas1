from flask import Flask, render_template, request, jsonify, send_file
import os
import tempfile
import base64
from ciphers import (
    ShiftCipher, SubstitutionCipher, AffineCipher, 
    VigenereCipher, HillCipher, PermutationCipher
)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        # Check if it's a file upload or JSON data
        if request.files:
            # File upload
            file = request.files['file']
            cipher_type = request.form.get('cipher_type')
            key = request.form.get('key', '')
            
            if not file or not cipher_type or not key:
                return jsonify({
                    'success': False,
                    'error': 'File, cipher type, dan key harus diisi'
                })
            
            # Pilih cipher berdasarkan tipe
            cipher = get_cipher_instance(cipher_type, key)
            
            # Baca file
            file_data = file.read()
            file_name = file.filename
            
            # Enkripsi file
            encrypted_data = cipher.encrypt_bytes(file_data)
            
            # Simpan file terenkripsi
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.dat')
            temp_file.write(encrypted_data)
            temp_file.close()
            
            return jsonify({
                'success': True,
                'message': 'File berhasil dienkripsi',
                'file_path': temp_file.name,
                'file_name': file_name + '.dat'
            })
        else:
            # JSON data (text encryption)
            data = request.get_json()
            cipher_type = data.get('cipher_type')
            text = data.get('text', '')
            key = data.get('key', '')
            
            # Pilih cipher berdasarkan tipe
            cipher = get_cipher_instance(cipher_type, key)
            
            # Enkripsi teks
            encrypted_text = cipher.encrypt(text)
            return jsonify({
                'success': True,
                'encrypted_text': encrypted_text
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        # Check if it's a file upload or JSON data
        if request.files:
            # File upload
            file = request.files['file']
            cipher_type = request.form.get('cipher_type')
            key = request.form.get('key', '')
            original_file_name = request.form.get('original_file_name', '')
            
            if not file or not cipher_type or not key:
                return jsonify({
                    'success': False,
                    'error': 'File, cipher type, dan key harus diisi'
                })
            
            # Pilih cipher berdasarkan tipe
            cipher = get_cipher_instance(cipher_type, key)
            
            # Baca file
            file_data = file.read()
            
            # Dekripsi file
            decrypted_data = cipher.decrypt_bytes(file_data)
            
            # Simpan file terdekripsi
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=original_file_name)
            temp_file.write(decrypted_data)
            temp_file.close()
            
            return jsonify({
                'success': True,
                'message': 'File berhasil didekripsi',
                'file_path': temp_file.name,
                'file_name': original_file_name
            })
        else:
            # JSON data (text decryption)
            data = request.get_json()
            cipher_type = data.get('cipher_type')
            text = data.get('text', '')
            key = data.get('key', '')
            
            # Pilih cipher berdasarkan tipe
            cipher = get_cipher_instance(cipher_type, key)
            
            # Dekripsi teks
            decrypted_text = cipher.decrypt(text)
            return jsonify({
                'success': True,
                'decrypted_text': decrypted_text
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

def get_cipher_instance(cipher_type, key):
    """Mengembalikan instance cipher berdasarkan tipe"""
    if cipher_type == 'shift':
        return ShiftCipher(int(key) if key.isdigit() else 0)
    elif cipher_type == 'substitution':
        return SubstitutionCipher(key)
    elif cipher_type == 'affine':
        a, b = map(int, key.split(',')) if ',' in key else (1, 0)
        return AffineCipher(a, b)
    elif cipher_type == 'vigenere':
        return VigenereCipher(key)
    elif cipher_type == 'hill':
        return HillCipher(key)
    elif cipher_type == 'permutation':
        return PermutationCipher(key)
    else:
        raise ValueError(f"Tipe cipher tidak valid: {cipher_type}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
