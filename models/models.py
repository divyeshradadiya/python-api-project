from pydantic import BaseModel
from typing import List

class ItemDetail(BaseModel):
    item_name: str
    size: str
    price: float
    qty: int
    total: float

class PaymentDetail(BaseModel):
    payment_date: str
    payment_id: int
    amount: float
    due: float
    tips: float
    discount: float
    total_paid: float
    payment_type: str
    payment_status: str

class OrderDetail(BaseModel):
    order_id: int
    order_date: str
    order_status: str
    total_amount: float
    items: List[ItemDetail]
    payments: List[PaymentDetail]

class OrdersResponse(BaseModel):
    orders: List[OrderDetail]