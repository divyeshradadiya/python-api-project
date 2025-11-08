# Restaurant Orders API

A FastAPI-based REST API for retrieving restaurant orders with detailed item and payment information.

## Features

- List all orders with complete details including items and payments
- Secure API with Bearer token authentication
- SQLite database with sample restaurant data
- Automatic API documentation with OpenAPI/Swagger

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **SQLite**: Lightweight database
- **Pydantic**: Data validation

## Project Structure

```
python-api/
├── main.py                 # FastAPI application entry point
├── database/               # Database models and data
│   ├── __init__.py
│   ├── database.py         # SQLAlchemy models
│   └── data.py             # Sample data
├── models/                 # Pydantic response models
│   ├── __init__.py
│   └── models.py
├── services/               # Business logic services
│   ├── __init__.py
│   └── orders_service.py   # Orders retrieval logic
├── scripts/                # Utility scripts
│   ├── __init__.py
│   └── insert_data.py      # Database seeding script
├── requirements.txt        # Python dependencies
├── restaurant.db           # SQLite database file
└── README.md
```

## Setup

### Prerequisites

- Python 3.9+
- pip

### Installation

1. Clone or navigate to the project directory
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```bash
   python scripts/insert_data.py
   ```

## Running the API

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- Interactive API docs: `http://localhost:8000/docs`
- OpenAPI schema: `http://localhost:8000/openapi.json`

## Authentication

The API uses Bearer token authentication. Include the token in the Authorization header:

```
Authorization: Bearer secret-api-key
```

## Endpoints

### GET /orders

Retrieves all orders with detailed information.

**Response:**
```json
{
  "orders": [
    {
      "order_id": 10,
      "order_date": "01 Oct 2025",
      "order_status": "Completed",
      "total_amount": 9.25,
      "items": [
        {
          "item_name": "Item2",
          "size": "",
          "price": 2.5,
          "qty": 1,
          "total": 2.5
        }
      ],
      "payments": [
        {
          "payment_date": "01 Oct 2025",
          "payment_id": 100,
          "amount": 9.25,
          "due": 0.0,
          "tips": 0.0,
          "discount": 0.0,
          "total_paid": 9.25,
          "payment_type": "Card",
          "payment_status": "Completed"
        }
      ]
    }
  ]
}
```

## Database Schema

- **menus**: Menu categories (Food, Drinks)
- **categories**: Item categories (Starters, Mains, etc.)
- **menu_items**: Menu items with names, sizes, and prices
- **order_items**: Individual order line items
- **payments**: Payment transactions for orders

## Testing

Use tools like Postman or curl to test the API:

```bash
curl -H "Authorization: Bearer secret-api-key" http://localhost:8000/orders
```

To reseed the database with sample data:
```bash
python scripts/insert_data.py
```