# CipherPro - Modern Text Encryption Web Application

![CipherPro Banner](https://via.placeholder.com/1200x300/0a1929/00c8ff?text=CipherPro)

## Overview

CipherPro is a sleek, modern web application that allows users to encrypt and decrypt text using various cryptographic algorithms. Built with Flask and Python's cryptography libraries, this application provides a user-friendly interface for text encryption with a futuristic design.

**Created by:** MHassan  
**Last Updated:** 2025-10-22

## Features

- **Multiple Encryption Algorithms:**
  - Caesar Cipher (with decryption)
  - AES (Advanced Encryption Standard)
  - Base64 Encoding/Decoding
  - SHA-256 Hashing
  - RSA Encryption
  - Fernet Symmetric Encryption

- **Modern User Interface:**
  - Sleek, futuristic design with dark theme
  - Responsive layout for all devices
  - Interactive animations and effects
  - Real-time feedback

- **User Experience:**
  - Copy results to clipboard with one click
  - Clear error messaging
  - Input validation
  - Loading animations during processing

## Screenshots

![CipherPro Interface](https://via.placeholder.com/800x500/132f4c/00c8ff?text=CipherPro+Interface)

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/cipherpro.git
cd cipherpro
```

2. **Create and activate a virtual environment:**

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the application:**

```bash
python app.py
```

5. **Access the application:**
Open your web browser and navigate to `http://127.0.0.1:5000/`

## Project Structure

```
cipherpro/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css      # Application styling
│   └── js/
│       └── script.js      # Frontend JavaScript logic
└── templates/
    └── index.html         # Main HTML template
```

## Encryption Techniques

### Caesar Cipher
A substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet (shift of 3 in this implementation).

### AES (Advanced Encryption Standard)
A symmetric encryption algorithm using a 256-bit key with Cipher Block Chaining (CBC) mode and proper initialization vectors.

### Base64
A binary-to-text encoding scheme that represents binary data in ASCII string format.

### SHA-256
A cryptographic hash function that produces a 256-bit hash value, commonly used for password storage and verifying data integrity.

### RSA
An asymmetric encryption algorithm that uses public-key cryptography for secure data transmission.

### Fernet
A symmetric encryption implementation that guarantees that a message encrypted cannot be manipulated or read without the key.

## Use Cases

- Securely share sensitive information
- Learn about different encryption algorithms
- Generate hashes for password storage
- Encode binary data for transmission over text channels
- Educational tool for understanding cryptography basics

## Security Note

While this application implements several strong encryption algorithms, it is primarily designed for educational purposes. For production environments or security-critical applications, please consider:

- Implementing secure key management
- Using dedicated encryption libraries directly
- Being aware that web-based encryption tools may expose keys in browser memory

## Dependencies

- Flask==2.0.1
- Werkzeug==2.0.1
- cryptography==36.0.0

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [cryptography](https://cryptography.io/) - Python library for cryptographic recipes
- Modern UI inspiration from various cybersecurity tools

---

Made with ❤️ by MHassan | [GitHub](https://github.com/yourusername) | [Website](https://yourwebsite.com)