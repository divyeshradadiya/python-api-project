from database.database import SessionLocal, Menu, Category, MenuItem, OrderItem, Payment
from database.data import menus, categories, menu_items, order_items, payments

def insert_data():
    db = SessionLocal()
    try:
        # Delete existing data
        # db.query(Payment).delete()
        # db.query(OrderItem).delete()
        # db.query(MenuItem).delete()
        # db.query(Category).delete()
        # db.query(Menu).delete()
        # db.commit()
        
        # Insert menus
        for m in menus:
            db_menu = Menu(id=m["id"], name=m["name"])
            db.add(db_menu)
        
        # Insert categories
        for c in categories:
            db_cat = Category(id=c["id"], name=c["name"], menu_id=c["menu_id"])
            db.add(db_cat)
        
        # Insert menu items
        for mi in menu_items:
            db_mi = MenuItem(id=mi["id"], name=mi["name"], cat_id=mi["cat_id"], menu_id=mi["menu_id"], sizes=mi["sizes"], prices=mi["prices"])
            db.add(db_mi)
        
        # Insert order items
        for oi in order_items:
            db_oi = OrderItem(
                id=oi["id"], order_date=oi["order_date"], order_id=oi["order_id"], item_id=oi["item_id"],
                size=oi["size"], price=oi["price"], qty=oi["qty"], order_status=oi["order_status"], total=oi["total"]
            )
            db.add(db_oi)
        
        # Insert payments
        for p in payments:
            db_p = Payment(
                id=p["id"], payment_date=p["payment_date"], payment_id=p["payment_id"], order_id=p["order_id"],
                amount=p["amount"], due=p["due"], tips=p["tips"], discount=p["discount"], total_paid=p["total_paid"],
                payment_type=p["payment_type"], payment_status=p["payment_status"]
            )
            db.add(db_p)
        
        db.commit()
        print("Data inserted successfully")
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    insert_data()