# =================================================================
# MODULE: crypto/encryption.py
# PURPOSE: Handle all Fernet AES encryption and key management.
# =================================================================

import os
from cryptography.fernet import Fernet

KEY_FILE = "secure_key.key"

def load_or_create_key():
    """Ensures an encryption key exists and returns it."""
    if not os.path.exists(KEY_FILE):
        with open(KEY_FILE, "wb") as f:
            f.write(Fernet.generate_key())
    
    with open(KEY_FILE, "rb") as f:
        return f.read()

# Initialize the Fernet engine once for the whole app to use
_key = load_or_create_key()
cipher_suite = Fernet(_key)

def encrypt_password(plaintext_password: str) -> bytes:
    """Converts string password to encrypted bytes."""
    return cipher_suite.encrypt(plaintext_password.encode())

def decrypt_password(encrypted_password: bytes) -> str:
    """Converts encrypted bytes back to a readable string."""
    return cipher_suite.decrypt(encrypted_password).decode()
