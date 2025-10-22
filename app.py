from flask import Flask, render_template, request, jsonify
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

app = Flask(__name__)

# Secret key for session
app.secret_key = os.urandom(24)


# Caesar Cipher implementation
def caesar_cipher(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result


# AES implementation
def aes_encrypt(text, key=None):
    if key is None:
        key = os.urandom(32)  # 256-bit key
    iv = os.urandom(16)  # 128-bit IV

    # Ensure the text is a multiple of 16 bytes (AES block size)
    while len(text.encode()) % 16 != 0:
        text += " "

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(text.encode()) + encryptor.finalize()

    # Return base64 encoded values for display
    return base64.b64encode(iv + key + ciphertext).decode('utf-8')


# Base64 encoding
def base64_encode(text):
    return base64.b64encode(text.encode()).decode('utf-8')


# SHA-256 hashing
def sha256_hash(text):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(text.encode())
    return digest.finalize().hex()


# RSA placeholder (simplified for demo)
def rsa_encrypt(text):
    # In a real app, you'd use proper RSA implementation
    # This is just a placeholder
    return base64.b64encode(text.encode()).decode('utf-8') + " (RSA Placeholder)"


# Fernet (symmetric encryption)
def fernet_encrypt(text):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(text.encode())
    # Return both the key and cipher text (in real app, secure the key)
    return f"Key: {key.decode()}, Ciphertext: {cipher_text.decode()}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    text = data.get('text', '')
    algorithm = data.get('algorithm', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    if not algorithm:
        return jsonify({"error": "No algorithm selected"}), 400

    result = ""
    if algorithm == "caesar":
        result = caesar_cipher(text)
    elif algorithm == "aes":
        result = aes_encrypt(text)
    elif algorithm == "base64":
        result = base64_encode(text)
    elif algorithm == "sha256":
        result = sha256_hash(text)
    elif algorithm == "rsa":
        result = rsa_encrypt(text)
    elif algorithm == "fernet":
        result = fernet_encrypt(text)
    else:
        return jsonify({"error": "Invalid algorithm"}), 400

    return jsonify({"result": result})


@app.route('/decrypt', methods=['POST'])
def decrypt():
    # Simplified decryption handling - in a real application, you'd implement
    # proper decryption for each algorithm
    data = request.json
    text = data.get('text', '')
    algorithm = data.get('algorithm', '')

    if algorithm == "caesar":
        # For Caesar, we can decrypt by shifting in the opposite direction
        result = caesar_cipher(text, shift=23)  # 26 - 3 = 23
        return jsonify({"result": result})
    elif algorithm == "base64":
        try:
            result = base64.b64decode(text).decode('utf-8')
            return jsonify({"result": result})
        except:
            return jsonify({"error": "Invalid Base64 string"}), 400
    else:
        # For other algorithms, proper decryption would require the key
        return jsonify({"error": "Decryption not implemented for this algorithm"}), 501


if __name__ == '__main__':
    app.run(debug=True)