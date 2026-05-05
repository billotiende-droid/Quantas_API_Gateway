import asyncio
from pathlib import Path
import sqlite3
import time
from typing import Dict, List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

DATABSE_PATH = Path(__file__).with_name("quantas.db")

app = FastAPI(title="Quantas API Gateway")

app.add_middleware (
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# database connection helper
def get_db_data(user_id: int):
    conn = sqlite3.connect(DATABSE_PATH)
    conn.row_factory = sqlite3.Row  # Enable access columns by name
    try:
        cursor = conn.cursor()

        # JOIN users and wallets to get all wallet info for the user
        query = """
        SELECT users.username as user, wallets.currency, wallets.balance
        FROM users
        JOIN wallets ON users.id = wallets.user_id
        WHERE users.id = ?
        """
        cursor.execute(query, (user_id,))
        rows = cursor.fetchall()
    finally:
        conn.close()    

