"""Main module of finance application"""
from typing import List
from fastapi import  FastAPI

from finance_project.database.database import SessionLocal

from finance_project.models.user_request_stock import Stock

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/stocks")
def get_stocks():
    print(str(stocks))
    return stocks

@app.post("/stocks/create-stock")
def create_stock(stock_body: StockSchema):
    stock =  Stock(**stock_body.model_dump())
    stocks.append(stock)