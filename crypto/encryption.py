KEY_FILE = "secure_key.key"  # File for storing the encryption key
MASTER_USERS = {"admin": "SecureSphere2026"}  # Default admin login credentials

# --- ENCRYPTION ---
# Generate and save a key if KEY_FILE doesn't exist
if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(Fernet.generate_key())  # Generate a secure key

# Load the encryption key
with open(KEY_FILE, "rb") as key_file:
    ENCRYPTION_KEY = key_file.read()

# Initialize Fernet for encryption and decryption
fernet = Fernet(ENCRYPTION_KEY)

