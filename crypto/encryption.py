# ================================================================
# SecureSphere Innovations
# Secure Password Manager
#
# Made by Collaborative-Fidelity
# Copyright (c) 2026 Collaborative-Fidelity
# All Rights Reserved.
#
# Module: encryption.py
# Purpose: Centralized encryption and decryption logic
# ================================================================

import os
from cryptography.fernet import Fernet

KEY_FILE = "secure_key.key"

def load_or_create_key() -> bytes:
    """
    Loads an existing encryption key or creates one if missing.
    """
    if not os.path.exists(KEY_FILE):
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(Fernet.generate_key())

    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

# Initialize Fernet instance once
FERNET = Fernet(load_or_create_key())

def encrypt_password(plaintext_password: str) -> bytes:
    """
    Encrypt a plaintext password.
    """
    return FERNET.encrypt(plaintext_password.encode())

def decrypt_password(encrypted_password: bytes) -> str:
    """
    Decrypt an encrypted password.
    """
    return FERNET.decrypt(encrypted_password).decode()
