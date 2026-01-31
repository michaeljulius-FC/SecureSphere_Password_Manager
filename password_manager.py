# =================================================================
# COPYRIGHT: (c) 2026 Collective-Fidelity. All Rights Reserved.
# PROJECT: SecureSphere_Password_Manager
# DESCRIPTION: Advanced secure password storage and generation.
# =================================================================

import os  # For file operations (e.g., checking file existence)
import string  # For combining letter, digit, and punctuation sets
from datetime import datetime  # For logging timestamps
from cryptography.fernet import Fernet  # For encryption and decryption of passwords
import secrets  # Cryptographically secure random number module (for passwords)

# --- CONSTANTS ---
PASSWORD_FILE = "passwords.txt"
LOG_FILE = "logs.txt"
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

# --- LOGGING FUNCTION ---
def log_action(user, action):
    """
    PURPOSE: Security Auditing.
    WHAT HAPPENS: Opens 'logs.txt' in append mode ('a') so we don't erase history.
    It writes a timestamp, the user, and the action performed.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current timestamp
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] USER: {user} | ACTION: {action}\n")

# --- ENCRYPTION/DECRYPTION FUNCTIONALITY ---
def encrypt_password(plaintext_password):
    """
    PURPOSE: Encrypts the given plaintext password.
    INPUT: A plaintext password.
    OUTPUT: The encrypted password (as a

