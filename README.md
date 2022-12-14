# Clickit - IT E-Commerce Platform

## Description

E-Commerce Website for selling and purchasing of hardware and software components related to devices such as computers, mobiles, tablets, etc.
The website will provide a common platform for sellers and interested buyers of technical devices and computing devices to connect.

Sellers can register items they wish to sell over the platform for purchase by customers.
Customers may search and choose items that they desire based on best features.
Items include computing devices such as computers, tablets or smartwatches, and/or accessories & spare-parts related to these devices.

## Features

### Must-have Features:

1. Authentication: Login, register as seller, register as customer
2. Registration of items for selling (name, category, sub-category, quantity, expected price)
3. Order management: view, confirm orders
4. Cart management: Add, remove, view items
5. Item management: view items with details (name, category, price, rating) (add item to cart) (rate purchased item)
6. Item search and filter: (specific, category/sub-category wise, filters over properties)

### Good-to-have Features:

1. Real-Time Order tracking
2. Recommendations based on product purchase and frequent user purchases
3. Product comparison for best deals / best features
4. Fuzzy Filtering

### Technical Stack:

#### Frontend
- HTML + CSS + JavaScript for dynamic front-end content
#### Backend
- Flask (Python) (for route handling and dispatch)
- SQLAlchemy (Python) (for interaction with an SQL-based DBMS)
- socket.io (Python, JS) for real-time updates
- MySQL for DBMS

### Project Details:
- [API Description](docs/api_description.md)
- [RDBMS Schema](docs/schema_description.md)