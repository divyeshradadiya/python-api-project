from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "sqlite:///./restaurant.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Menu(Base):
    __tablename__ = "menus"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    menu_id = Column(Integer, ForeignKey("menus.id"))

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    cat_id = Column(Integer, ForeignKey("categories.id"))
    menu_id = Column(Integer, ForeignKey("menus.id"))
    sizes = Column(String)
    prices = Column(String)

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_date = Column(String)
    order_id = Column(Integer, index=True)
    item_id = Column(Integer, ForeignKey("menu_items.id"))
    size = Column(String)
    price = Column(Float)
    qty = Column(Integer)
    order_status = Column(String)
    total = Column(Float)

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    payment_date = Column(String)
    payment_id = Column(Integer, index=True)
    order_id = Column(Integer, index=True)
    amount = Column(Float)
    due = Column(Float)
    tips = Column(Float)
    discount = Column(Float)
    total_paid = Column(Float)
    payment_type = Column(String)
    payment_status = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()