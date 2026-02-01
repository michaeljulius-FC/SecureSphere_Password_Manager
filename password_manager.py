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

from crypto.encryption import encrypt_password

PASSWORD_FILE = "passwords.txt"
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
# Password Storage (temporary file-based)
# ------------------------------------------------
def store_password(service: str, username: str, encrypted_password: bytes):
    with open(PASSWORD_FILE, "ab") as f:
        record = f"{service}|{username}|".encode() + encrypted_password + b"\n"
        f.write(record)

# ------------------------------------------------
# Main Execution
# ------------------------------------------------
def main():
    user = "admin"

    service = "example.com"
    username = "admin_user"

    password = generate_password()
    encrypted = encrypt_password(password)

    store_password(service, username, encrypted)
    log_action(user, f"Stored password for {service}")

    print("Password generated and stored securely.")
    print("Generated password (displayed once):", password)

if __name__ == "__main__":
    main()

