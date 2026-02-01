import string
import secrets
import hashlib
import sys
from datetime import datetime

# Import modules
try:
    from crypto.encryption import encrypt_password, decrypt_password
    from vault.storage import init_db, store_password, retrieve_password, delete_password
    print("--- [SYSTEM] Encryption & Vault Modules Loaded ---")
except ImportError:
    print("--- [ERROR] Check folder structure and __init__.py files ---")

LOG_FILE = "logs.txt"

def log_action(user: str, action: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] USER: {user} | ACTION: {action}\n")

def login():
    """Requires a master password to enter the program."""
    try:
        with open("master.hash", "r") as f:
            stored_hash = f.read().strip()
    except FileNotFoundError:
        print("[ERROR] No master password found. Run setup_master.py first.")
        sys.exit()

    attempts = 3
    while attempts > 0:
        password = input(f"\n[SECURE LOGIN] Enter Master Password ({attempts} attempts left): ")
        input_hash = hashlib.sha256(password.encode()).hexdigest()
        
        if input_hash == stored_hash:
            print("Access Granted.")
            return True
        else:
            attempts -= 1
            print("Invalid Password.")
    
    print("Too many failed attempts. Security Lockdown.")
    sys.exit()

def generate_password(length: int = 16) -> str:
    charset = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(charset) for _ in range(length))

def create_new_entry():
    service = input("Enter the service name: ")
    username = input("Enter the username: ")
    password = generate_password()
    encrypted = encrypt_password(password)
    store_password(service, username, encrypted)
    log_action("admin", f"Created password for {service}")
    print(f"\n[SUCCESS] Saved: {password}")

def find_existing_entry():
    service = input("Enter the service name to search for: ")
    username = input("Enter the username: ")
    encrypted_pwd = retrieve_password(service, username)
    if encrypted_pwd:
        decrypted = decrypt_password(encrypted_pwd)
        print(f"\n[FOUND] Password: {decrypted}")
    else:
        print("\n[NOT FOUND] No record exists.")

def remove_entry():
    service = input("Enter the service name to DELETE: ")
    username = input("Enter the username: ")
    confirm = input(f"Are you sure you want to delete {service}? (y/n): ")
    if confirm.lower() == 'y':
        if delete_password(service, username):
            log_action("admin", f"DELETED {service}")
            print(f"\n[DELETED] Record removed.")
        else:
            print("\n[ERROR] Record not found.")

def main():
    init_db()
    # THE GATEKEEPER
    if login():
        while True:
            print("\n--- SecureSphere Password Manager ---")
            print("1. Generate & Save New Password")
            print("2. Search for Existing Password")
            print("3. Delete a Password")
            print("4. Exit")
            
            choice = input("\nSelect (1-4): ")
            if choice == "1": create_new_entry()
            elif choice == "2": find_existing_entry()
            elif choice == "3": remove_entry()
            elif choice == "4": break
            else: print("Invalid selection.")

if __name__ == "__main__":
    main()
