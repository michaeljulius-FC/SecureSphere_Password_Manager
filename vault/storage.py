import sqlite3

DB_FILE = "vault/passwords.db"

def init_db():
    """Initializes the database and creates the passwords table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            encrypted_password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def store_password(service, username, encrypted_pwd):
    """Stores a new encrypted password in the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO credentials (service, username, encrypted_password)
        VALUES (?, ?, ?)
    ''', (service, username, encrypted_pwd))
    conn.commit()
    conn.close()

def retrieve_password(service, username):
    """Retrieves an encrypted password for a specific service and user."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT encrypted_password FROM credentials 
        WHERE service = ? AND username = ?
    ''', (service, username))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def update_password(service, username, new_encrypted_pwd):
    """Updates the password for an existing service and username."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # The UPDATE command changes data in an existing row instead of adding a new one
    cursor.execute('''
        UPDATE credentials 
        SET encrypted_password = ? 
        WHERE service = ? AND username = ?
    ''', (new_encrypted_pwd, service, username))
    conn.commit()
    changes = conn.total_changes
    conn.close()
    return changes > 0

def delete_password(service, username):
    """Removes a specific credential from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM credentials 
        WHERE service = ? AND username = ?
    ''', (service, username))
    conn.commit()
    changes = conn.total_changes
    conn.close()
    return changes > 0

def list_all_services():
    """Retrieves all service names and usernames from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT service, username FROM credentials')
    results = cursor.fetchall()
    conn.close()
    return results
