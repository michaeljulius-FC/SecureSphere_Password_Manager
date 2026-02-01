# ================================================================
# SecureSphere Innovations
# Secure Password Manager
#
# Made by Collaborative-Fidelity
# Copyright (c) 2026 Collaborative-Fidelity
# All Rights Reserved.
#
# Module: storage.py
# Purpose: Handles secure storage of encrypted passwords
# ================================================================

import sqlite3

DB_FILE = "vault.db"

def init_db():
    """Initialize the SQLite database and create table if missing."""
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                username TEXT NOT NULL,
                password BLOB NOT NULL
            )
        """)

def store_password(service: str, username: str, encrypted_password: bytes):
    """Store an encrypted password for a given service and username."""
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            "INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
            (service, username, encrypted_password)
        )

def retrieve_password(service: str, username: str):
    """Retrieve the encrypted password for a service and username."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute(
            "SELECT password FROM passwords WHERE service=? AND username=?",
            (service, username)
        )
        row = cursor.fetchone()
        return row[0] if row else None
