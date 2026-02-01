# =================================================================
# SecureSphere Innovations
# Secure Password Manager
#
# Made by Collaborative-Fidelity
# Copyright (c) 2026 Collaborative-Fidelity
# All Rights Reserved.
# =================================================================

import string
import secrets
from datetime import datetime

# Import modules from your project folders
try:
    from crypto.encryption import encrypt_password, decrypt_password
    from vault.storage import init_db, store_password, retrieve_password
    print("--- [SYSTEM] Encryption & Vault Modules Loaded ---")
except ImportError:
    print("--- [ERROR] Could not find project modules ---")
    print("--- Ensure you have __init__.py files in crypto and vault folders ---")

LOG_FILE = "logs.txt"

# --- Logging ---
def log_action(user: str, action: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] USER: {user} | ACTION: {action}\n")

# --- Password Generator ---
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

# --- Main Execution ---
def main():
    # Initialize the database (creates table if missing)
    try:
        init_db()
    except NameError:
        print("[SKIP] Database initialization skipped (vault module not ready).")

    user = "admin"
    service = "example.com"
    username = "admin_user"

    print("\n--- SecureSphere Password Manager Starting ---")

    # 1. Generate and encrypt password
    password = generate_password()
    print(f"Generated New Password: {password}")
    
    encrypted = encrypt_password(password)
    print(f"Encrypted Version: {encrypted}")

    # 2. Store in SQLite vault
    try:
        store_password(service, username, encrypted)
        log_action(user, f"Stored password for {service}")
        print("Password stored and logged successfully.")
    except NameError:
        print("[ERROR] Could not store password (vault functions missing).")

    # 3. Demonstration: retrieving the password
    try:
        retrieved_enc = retrieve_password(service, username)
        if retrieved_enc:
            decrypted = decrypt_password(retrieved_enc)
            print(f"Decrypted Password for {service}: {decrypted}")
    except NameError:
        pass

    print("\n--- SecureSphere Process Complete ---")

# --- THE START BUTTON ---
# This part MUST be at the very bottom and have NO spaces before it.
if __name__ == "__main__":
    main()
