# ================================================================
# SecureSphere Innovations
# Secure Password Manager
#
# Made by Collaborative-Fidelity
# Copyright (c) 2026 Collaborative-Fidelity
# All Rights Reserved.
# ================================================================

import string
import secrets
from datetime import datetime

from crypto.encryption import encrypt_password, decrypt_password
from vault.storage import init_db, store_password, retrieve_password
LOG_FILE = "logs.txt"

# ------------------------------------------------
# Logging
# ------------------------------------------------
def log_action(user: str, action: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] USER: {user} | ACTION: {action}\n")

# ------------------------------------------------
# Password Generator
# ------------------------------------------------
def generate_password(length: int = 16) -> str:
    if length < 12:
        raise ValueError("Password length must be at least 12 characters")

    charset = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    return ''.join(secrets.choice(charset) for _ in range(length))

# ------------------------------------------------
# Main Execution
# ------------------------------------------------
def main():
    # Initialize the database (creates table if missing)
    init_db()

    user = "admin"
    service = "example.com"
    username = "admin_user"

    # Generate and encrypt password
    password = generate_password()
    encrypted = encrypt_password(password)

    # Store in SQLite vault
    store_password(service, username, encrypted)
    log_action(user, f"Stored password for {service}")

    # Demonstration: retrieving the password (optional)
    retrieved_enc = retrieve_password(service, username)
    if retrieved_enc:
        decrypted = decrypt_password(retrieved_enc)
        prin

