# Quantas API Gateway
Quantas API Gateway Quantas API Gateway is a high-performance, asynchronous settlement engine designed for real-time multi-currency reconciliation. This project demonstrates a decoupled full-stack architecture focusing on concurrency, data integrity, and type safety.

Full-stack demo with a Next.js dashboard and a FastAPI settlement API backed by SQLite.

## Setup

Install frontend dependencies:

```bash
npm install
```

Install backend dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn pydantic
```

## Initialize Data

Run the seed script from the backend folder so `backend/quantas.db` is created:

```bash
cd backend
python seed.py
```

## Run

Start the API:

```bash
cd backend
uvicorn main:app --reload --port 8000
```

In another terminal, start the frontend:

```bash
npm run dev
```

Open `http://localhost:3000`.

## Useful Commands

```bash
npm run lint
npm run build
```

API endpoint: `http://localhost:8000/api/v1/settlement/1`
