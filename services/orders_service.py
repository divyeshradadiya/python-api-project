from sqlalchemy.orm import Session
from database.database import OrderItem, Payment, MenuItem

def get_all_orders(db: Session):
    # Get unique order_ids
    order_ids = db.query(OrderItem.order_id).distinct().all()
    orders = []
    for (oid,) in order_ids:
        # Get order items with menu names
        items_query = db.query(OrderItem, MenuItem.name).join(MenuItem, OrderItem.item_id == MenuItem.id).filter(OrderItem.order_id == oid).all()
        item_details = [
            {
                "item_name": name,
                "size": item.size,
                "price": item.price,
                "qty": item.qty,
                "total": item.total
            } for item, name in items_query
        ]
        # Get payments
        payments_query = db.query(Payment).filter(Payment.order_id == oid).all()
        payment_details = [
            {
                "payment_date": p.payment_date,
                "payment_id": p.payment_id,
                "amount": p.amount,
                "due": p.due,
                "tips": p.tips,
                "discount": p.discount,
                "total_paid": p.total_paid,
                "payment_type": p.payment_type,
                "payment_status": p.payment_status
            } for p in payments_query
        ]
        # Order details from first item
        order_date = items_query[0][0].order_date
        order_status = items_query[0][0].order_status
        total_amount = sum(item.total for item, _ in items_query)
        orders.append({
            "order_id": oid,
            "order_date": order_date,
            "order_status": order_status,
            "total_amount": total_amount,
            "items": item_details,
            "payments": payment_details
        })
    return orders