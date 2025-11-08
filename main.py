from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from database.database import get_db
from models.models import OrdersResponse
from services.orders_service import get_all_orders

app = FastAPI(title="Restaurant Orders API", description="API to list orders with payment and item details", version="1.0.0")

bearer = HTTPBearer()

def verify_api_key(credentials = Depends(bearer)):
    # In production, use environment variable
    if credentials.credentials != "secret-api-key":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return credentials.credentials

@app.get("/orders", response_model=OrdersResponse, dependencies=[Depends(verify_api_key)])
def get_orders(db: Session = Depends(get_db)):
    orders = get_all_orders(db)
    return {"orders": orders}