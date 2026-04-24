from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_URL = "https://api.twelvedata.com"
API_KEY = os.getenv("TWELVE_API_KEY")

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.get("/stocks/movers")
async def market_movers():
    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{BASE_URL}/market_movers/stocks",
            params={"apikey": API_KEY}
        )
        return res.json()

@app.get("/stocks/price/{symbol}")
async def price(symbol: str):
    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{BASE_URL}/price",
            params={"symbol": symbol, "apikey": API_KEY}
        )
        return res.json()

@app.get("/stocks/quote/{symbol}")
async def quote(symbol: str):
    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{BASE_URL}/quote",
            params={"symbol": symbol, "apikey": API_KEY}
        )
        return res.json()

@app.get("/stocks/history/{symbol}")
async def history(symbol: str):
    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{BASE_URL}/time_series",
            params={
                "symbol": symbol,
                "interval": "1day",
                "outputsize": 30,
                "apikey": API_KEY
            }
        )
        return res.json()
