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