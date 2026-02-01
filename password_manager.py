# =================================================================
# PROJECT: SecureSphere_Password_Manager
# DESCRIPTION: Main orchestration script with Start-Up Check.
# =================================================================

import os
import secrets
import string
from datetime import datetime

# Import modules from your project folders
try:
    from crypto.encryption import encrypt_password, decrypt_password
    # These will work once we add the vault logic in the next step
    # from vault.storage import init_db, store_password, retrieve_password
    print("--- [SYSTEM] Encryption Modules Loaded Successfully ---")
except ImportError:
    print("--- [ERROR] Could not find project modules ---")
    print("--- Ensure you have __init__.py files in crypto and vault folders ---")

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
    if length < 12:
        length = 12
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
        log_action(current_user, f"Generated and Encrypted a new password.")
        print("Action Logged Successfully.")
        
        # 4. Success Message
        print("\n--- SecureSphere Process Complete ---")
        
    except NameError:
        print("\n[CRITICAL ERROR] Encryption functions are not available.")
        print("Check that crypto/encryption.py exists and is correct.")

# --- THE TRIGGER ---
# This is the "Start Button" that was missing or broken in your previous version
if __name__ == "__main__":
    main()
