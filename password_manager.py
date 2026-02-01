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
from crypto.vault import init_db, store_password, retrieve_password

LOG_FILE = "logs.txt"

# ------------------------------------------------
# Logging
# ------------------------------------------------
def log_action(user: str, action: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] USER: {user} | ACTION: {action}\n")
    except Exception as e:
        print("ERROR writing to log file:", e)

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
    print("Starting SecureSphere Password Manager...")  # Debug print

    # Initialize the database (creates table if missing)
    try:
        init_db()
        print("Database initialized successfully.")
    except Exception as e:
        print("ERROR initializing database:", e)
        return

    user = "admin"
    service = "example.com"
    username =
