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
    return [dict(row) for row in rows]   

# IMPROVEMENT : Pydantic Validation
# This ensures "Money" stays "Money" (No weird strings) 
class WalletSchema(BaseModel):
    currency : str
    balance : float
    user : str

class SettlementResponse(BaseModel):
    status : str
    data : List[WalletSchema]
    rates : Dict[str, float]
    cached : bool
# Caching logic
# Store rates in memory so we dont fetch them every time (Fast and Cheap)
rate_cache = {"data": None, "expiry": 0}    

async def fetch_market_rates():
    current_time = time.time()
    if rate_cache["data"] and current_time < rate_cache["expiry"]:
        return rate_cache["data"], True  # Return cached data and indicate it's from cache
    
    # simulate fetching from external API (replace with real API call)
    await asyncio.sleep(1)  # Simulate network delay
    new_rates = {"USD": 1.0, "BTC": 0.000015}  # Mocked rates

    # Cached for 60 seconds
    rate_cache["data"] = new_rates
    rate_cache["expiry"] = current_time + 60
    return new_rates, False  # Return new data and indicate it's not from cache

@app.get("/api/v1/settlement/{user_id}", response_model=SettlementResponse)
async def get_settlement(user_id: int):
    #Concurrency : Fetch user data and market rates at the same time while reading settlement data from the database
    rates_task = asyncio.create_task(fetch_market_rates)

    # SQL: get real data from our JOIN
    db_data = get_db_data(user_id)
    rates, cached = await rates_task

    if not db_data:
        raise HTTPException(status_code=404, detail="Settlement data not found")
    
    return {
        "status": "success",
        "data": db_data,
        "rates": rates,
        "cached": cached
    }