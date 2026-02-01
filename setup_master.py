import hashlib

def create_master():
    password = input("Set your Master Password: ")
    # Scramble the password into a hash
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    with open("master.hash", "w") as f:
        f.write(hashed_password)
    print("Master password set successfully!")

if __name__ == "__main__":
    create_master()