import sqlite3

def init_db():
    conn = sqlite3.connect("quantas.db")
    cursor = conn.cursor()

    # 1. Create Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL
    )
    """)

    # 2. Create Wallets Table (The Relationship)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS wallets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        currency TEXT NOT NULL,
        balance REAL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)
