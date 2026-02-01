import hashlib
import sys
import os

# ... (Keep your imports for string, secrets, and vault at the top)

def login():
    """Mandatory check for the master password hash."""
    hash_path = "master.hash"
    
    if not os.path.exists(hash_path):
        print("[CRITICAL] Security hash missing. Run setup_master.py first!")
        sys.exit()

    with open(hash_path, "r") as f:
        stored_hash = f.read().strip()

    attempts = 3
    while attempts > 0:
        # This line MUST be here to prompt you
        password = input(f"\n[SECURE LOGIN] Enter Master Password ({attempts} attempts left): ")
        input_hash = hashlib.sha256(password.encode()).hexdigest()
        
        if input_hash == stored_hash:
            print("Access Granted.")
            return True
        else:
            attempts -= 1
            print("Invalid Password.")
    
    print("Lockdown initiated. Access Denied.")
    sys.exit()

def main():
    # 1. Start the Gatekeeper first
    if login():
        # 2. Only if login is successful, initialize and show menu
        from vault.storage import init_db
        init_db()
        
        while True:
            print("\n--- SecureSphere Password Manager ---")
            print("1. Generate & Save New Password")
            print("2. Search for Existing Password")
            print("3. Delete a Password")
            print("4. Exit")
            # ... (Rest of your menu logic)
