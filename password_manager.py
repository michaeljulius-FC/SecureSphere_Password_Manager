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
import sqlite3

from crypto.encryption import encrypt_password, decrypt_password

DB_FILE = "vault/passwords.db"
LOG_FILE = "logs/logs.txt"

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
# Database Functions
# ------------------------------------------------
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password BLOB NOT NULL,
            PRIMARY KEY (service, username)
        )
    ''')
    conn.commit()
    conn.close()

def store_password(service: str, username: str, encrypted_password: bytes):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO passwords (service, username, password)
        VALUES (?, ?, ?)
    ''', (service, username, encrypted_password))
    conn.commit()
    conn.close()

def retrieve_password(service: str, username: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT password FROM passwords
        WHERE service = ? AND username = ?
    ''', (service, username))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    return None

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

    # Print generated password (displayed once)
    print("Password generated and stored securely.")
    print("Generated password (displayed once):", password)

    # Demonstration: retrieving the password (optional)
    retrieved_enc = retrieve_password(service, username)
    if retrieved_enc:
        decrypted = decrypt_password(retrieved_enc)
        print("Retrieved password:", decrypted)

# ------------------------------------------------
# Run main if script executed directly
# ------------------------------------------------
if __name__ == "__main__":
    main()
