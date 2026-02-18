# SecureSphere_Password_Manager

Developed with care by *Collaborative-Fidelity*, **SecureSphere Innovations** is dedicated to providing top-tier protection against digital threats for businesses, financial institutions, and government agencies. One of the critical challenges our clients face is securely managing a wide range of application and domain passwords.

To address this, SecureSphere Innovations has implemented a **Secure Password Generator and Manager**. This solution empowers users to generate strong, random passwords while also providing a secure and intuitive interface for managing them. The system keeps logs of all ongoing tasks and integrates robust user authentication to ensure that only authorized personnel can:
- **Add**, **update**, **retrieve**, or **delete** passwords securely, and
- Ensure sensitive information remains easily accessible when needed while maintaining security.

Our approach leverages **modern security practices** to deliver both ease of use and the highest level of **protection against cyber threats**, offering users confidence in an increasingly complex digital world.
A secure, command-line-based password management system built with Python and SQLite3. [cite_start]This project focuses on **Collaborative Fidelity**, ensuring a modular design that prioritizes data integrity and industry-standard security practices[cite: 3, 4].

# SecureSphere Password Manager

A secure, command-line-based password management system built with Python and SQLite3. [cite_start]This project focuses on **Collaborative Fidelity**, ensuring a modular design that prioritizes data integrity and industry-standard security practices[cite: 3, 4].

## 🔐 Key Features

- [cite_start]**Master Authentication Gatekeeper**: Uses SHA-256 hashing to verify user identity before granting access to the vault[cite: 11, 12].
- [cite_start]**Hidden Password Input**: Utilizes the `getpass` module to mask the Master Password during login to prevent "shoulder surfing"[cite: 13].
- [cite_start]**Secure CRUD Operations**: Full capability to Search, Add, Update, and Delete credentials stored in an encrypted SQLite3 database[cite: 18, 19, 20].
- [cite_start]**Robust Password Generation**: Automatically generates 16-character secure passwords using the `secrets` library, or allows for custom manual entry[cite: 15, 16].
- [cite_start]**Action Logging**: Maintains a `logs.txt` file to track system activity and modifications for audit purposes[cite: 21, 22].

## 🛠️ Technology Stack

- **Language**: Python 3.x
- **Database**: SQLite3
- **Security**: SHA-256 Hashing, AES-style logic, and masked terminal inputs.

## 🚀 Getting Started

### Prerequisites
- Python installed on your machine.

### Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/your-username/SecureSphere_Password_Manager.git](https://github.com/your-username/SecureSphere_Password_Manager.git)
2. Initialize the Master Password: Run the setup script to create your local security fingerprint:

Bash
python setup_master.py

3. python password_manager.py


🛡️ Security Note
This project uses a .gitignore to ensure that sensitive local files—such as master.hash, secure_key.key, and passwords.db—are never uploaded to the public repository.
This will be used for future projects
