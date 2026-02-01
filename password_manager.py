# =================================================================
# PROJECT: SecureSphere_Password_Manager
# DESCRIPTION: Main orchestration script with Start-Up Check.
# =================================================================

import os
import secrets
import string
from datetime import datetime

# We are importing the functions from your /crypto folder
try:
    from crypto.encryption import encrypt_password, decrypt_password
    print("--- [SYSTEM] Encryption Modules Loaded Successfully ---")
except ImportError:
    print("--- [ERROR] Could not find crypto/encryption.py ---")
    print("--- Ensure you have an empty __init__.py in the crypto folder ---")

# --- CONSTANTS ---
LOG_FILE = "logs.txt"
MASTER_USERS = {"admin": "SecureSphere2026"}

# --- LOGGING ---
def log_action(user, action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] USER: {user} | ACTION: {action}\n")

# --- PASSWORD GENERATOR ---
def generate_secure_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# --- MAIN EXECUTION ---
def main():
    print("\n--- SecureSphere Password Manager Starting ---")
    current_user = "admin" 
    
    # 1. Generate a new password
    raw_pwd = generate_secure_password()
    print(f"Generated New Password: {raw_pwd}")

    # 2. Encrypt it
    try:
        encrypted_pwd = encrypt_password(raw_pwd)
        print(f"Encrypted Version: {encrypted_pwd}")

        # 3. Log the event
        log_action(current_user, "Generated and Encrypted a new password.")
        print("Action Logged Successfully.")
    except NameError:
        print("Critical Error: Encryption functions not defined. Check your imports.")

# --- THE TRIGGER ---
# This is the "Command" that tells Python to actually RUN the code above.
if __name__ == "__main__":
    main()
