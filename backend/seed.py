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

    # 3. Insert Mock Data
    cursor.execute("INSERT INTO users (username) VALUES ('Bill Otiende')")
    cursor.execute("INSERT INTO wallets (user_id, currency, balance) VALUES (1, 'USD', 1250.50)")
    cursor.execute("INSERT INTO wallets (user_id, currency, balance) VALUES (1, 'BTC', 0.042)")

    cursor.execute("INSERT INTO users (username) VALUES ('Laura Otiende')")
    cursor.execute("INSERT INTO wallets (user_id, currency, balance) VALUES (1, 'USD', 1250.50)")
    cursor.execute("INSERT INTO wallets (user_id, currency, balance) VALUES (1, 'BTC', 0.042)")
    
    conn.commit()
    conn.close()
    print("✅ Quantas Database Seeded!")

if __name__ == "__main__":
    init_db()