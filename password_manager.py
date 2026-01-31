# =================================================================
# COPYRIGHT: (c) 2026 Collective-Fidelity. All Rights Reserved.
# PROJECT: SecureSphere_Password_Manager
# DESCRIPTION: Advanced secure password storage and generation.
# =================================================================

import random
import string
import os
from datetime import datetime

# --- CONFIGURATION & GLOBAL VARIABLES ---
# We define these globally so they are easy to change later if needed.
PASSWORD_FILE = "passwords.txt"
LOG_FILE = "logs.txt"
# For this case study, we use a default admin user.
MASTER_USERS = {"admin": "SecureSphere2026"}

def log_action(user, action):
    """
    PURPOSE: Security Auditing.
    WHAT HAPPENS: Opens 'logs.txt' in append mode ('a') so we don't erase history.
    It writes a timestamp, the user, and the action performed.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] USER: {user} | ACTION: {action}\n")

def generate_random_password(length=12):
    """
    PURPOSE: Create unhackable credentials.
    WHAT HAPPENS: It combines letters (up/low), digits, and special symbols.
    It uses the random library to pick characters until it hits 12 digits.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def add_password(user):
    """
    PURPOSE: Feature 1 - Add Password.
    WHAT HAPPENS: Asks for a domain. If the password field is left empty,
    it automatically triggers our 12-digit random generator.
    """
    domain = input("Enter the Application/Domain name (e.g., GitHub): ")
    pwd = input("Enter password (leave blank to auto-generate): ")
    
    if not pwd:
        pwd = generate_random_password()
        print(f"[*] Generated Secure Password: {pwd}")

    with open(PASSWORD_FILE, "a") as f:
        f.write(f"{domain} | {pwd}\n")
    
    print(f"[!] Successfully saved credentials for {domain}.")
    log_action(user, f"Added password for {domain}")

def retrieve_passwords(user):
    """
    PURPOSE: Feature 2 - Retrieval.
    WHAT HAPPENS: Checks if the file exists first to prevent errors.
    If found, it reads every line and prints it to the console.
    """
    if not os.path.exists(PASSWORD_FILE):
        print("[!] No database found. Add a password first.")
        return

    print("\n" + "="*30)
    print("  STORED PASSWORDS  ")
    print("="*30)
    with open(PASSWORD_FILE, "r") as f:
        content = f.read()
        print(content if content else "The vault is empty.")
    log_action(user, "Viewed all passwords")

def update_password(user):
    """
    PURPOSE: Feature 3 - Update.
    WHAT HAPPENS: This reads the whole file into a list, finds the domain,
    changes that specific line, and then overwrites the file with the new list.
    """
    domain_to_update = input("Enter the domain to update: ")
    updated_lines = []
    found = False

    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as f:
            lines = f.readlines()
        
        for line in lines:
            if line.startswith(domain_to_update + " |"):
                new_pwd = generate_random_password()
                updated_lines.append(f"{domain_to_update} | {new_pwd}\n")
                found = True
            else:
                updated_lines.append(line)
        
        with open(PASSWORD_FILE, "w") as f:
            f.writelines(updated_lines)
            
    if found:
        print(f"[!] {domain_to_update} has been updated with a new secure password.")
        log_action(user, f"Updated {domain_to_update}")
    else:
        print("[X] Domain not found.")

def delete_password(user):
    """
    PURPOSE: Feature 4 - Delete.
    WHAT HAPPENS: Similar to update, but it simply EXCLUDES the line
    matching the domain when writing the data back to the file.
    """
    domain_to_delete = input("Enter the domain to delete: ")
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as f:
            lines = f.readlines()
        with open(PASSWORD_FILE, "w") as f:
            for line in lines:
                if not line.startswith(domain_to_delete + " |"):
                    f.write(line)
        print(f"[!] Deleted {domain_to_delete} if it existed.")
        log_action(user, f"Deleted {domain_to_delete}")

def main():
    """
    PURPOSE: The Master Controller (Menu Interface).
    WHAT HAPPENS: Greets the user, performs authentication, and 
    runs a loop that keeps the program open until the user chooses to exit.
    """
    print("="*50)
    print("  WELCOME TO SECURESPHERE_PASSWORD_MANAGER  ")
    print("="*50)

    # Simple Authentication System
    username = input("Enter Username: ")
    password = input("Enter Master Password: ")

    if username in MASTER_USERS and MASTER_USERS[username] == password:
        print(f"\n[+] Access Granted. Welcome, {username}.")
        log_action(username, "Logged In")

        while True:
            print("\n--- MAIN MENU ---")
            print("1. Add Password")
            print("2. Retrieve Passwords")
            print("3. Update Password (Auto-Gen)")
            print("4. Delete Password")
            print("9. Exit")
            
            choice = input("\nSelect an option (1-9): ")

            if choice == "1": add_password(username)
            elif choice == "2": retrieve_passwords(username)
            elif choice == "3": update_password(username)
            elif choice == "4": delete_password(username)
            elif choice == "9":
                print("[!] SecureSphere Session Closed. Stay safe!")
                log_action(username, "Logged Out")
                break
            else:
                print("[X] Invalid selection.")
    else:
        print("[X] Authentication Failed. Program Terminated.")

if __name__ == "__main__":
    main()
