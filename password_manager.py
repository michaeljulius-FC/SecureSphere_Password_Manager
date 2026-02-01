import string
import secrets
from datetime import datetime

# Import modules
try:
    from crypto.encryption import encrypt_password, decrypt_password
    from vault.storage import init_db, store_password, retrieve_password, delete_password
    print("--- [SYSTEM] Encryption & Vault Modules Loaded ---")
except ImportError:
    print("--- [ERROR] Check your folder structure and __init__.py files ---")

LOG_FILE = "logs.txt"

def log_action(user: str, action: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] USER: {user} | ACTION: {action}\n")

def generate_password(length: int = 16) -> str:
    charset = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(charset) for _ in range(length))

def create_new_entry():
    service = input("Enter the service name (e.g., Netflix): ")
    username = input("Enter the username: ")
    password = generate_password()
    encrypted = encrypt_password(password)
    store_password(service, username, encrypted)
    log_action("admin", f"Created new password for {service}")
    print(f"\n[SUCCESS] Password for {service} saved: {password}")

def find_existing_entry():
    service = input("Enter the service name to search for: ")
    username = input("Enter the username: ")
    encrypted_pwd = retrieve_password(service, username)
    if encrypted_pwd:
        decrypted = decrypt_password(encrypted_pwd)
        print(f"\n[FOUND] Password for {service} ({username}): {decrypted}")
    else:
        print(f"\n[NOT FOUND] No record for {service}.")

def remove_entry():
    """New logic to delete a record."""
    service = input("Enter the service name to DELETE: ")
    username = input("Enter the username: ")
    confirm = input(f"Are you sure you want to delete {service}? (y/n): ")
    
    if confirm.lower() == 'y':
        if delete_password(service, username):
            log_action("admin", f"DELETED record for {service}")
            print(f"\n[DELETED] Record for {service} has been removed.")
        else:
            print(f"\n[ERROR] No record found to delete for {service}.")

def main():
    init_db()
    while True:
        print("\n--- SecureSphere Password Manager ---")
        print("1. Generate & Save New Password")
        print("2. Search for Existing Password")
        print("3. Delete a Password")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")
        
        if choice == "1":
            create_new_entry()
        elif choice == "2":
            find_existing_entry()
        elif choice == "3":
            remove_entry()
        elif choice == "4":
            print("Exiting SecureSphere...")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
