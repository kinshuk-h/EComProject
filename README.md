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

### [API Description](docs/api_description.md):

- Authentication:
	- POST /api/auth/login: Login using an existing customer or seller account, init session
		- Parameters:
			- Customer ID | Customer Username | Customer E-Mail (One of any unique Identifiers)
			- Customer Account Password
		- Returns:
			Customer Account ID, Access Token, Expiration Duration (JSON)
	- POST /api/auth/refresh: Refresh login state, update login token
		- Headers:
			- Authentication: Bearer "<account_id>:<access_token>"
		- Returns:
			Customer Account ID, New Access Token, Updated Expiration Duration (JSON)
- Customers:
	- PUT /api/customer/register: Register a new customer
		- Parameters:
			- Customer Details (Name, etc.)
			- Customer Account Password (plaintext, over HTTPS, stored in DB as hash+salt)
	- GET /api/customer/<customer_id?>:
		- Headers:
			- Authentication: Bearer "<account_id>:<access_token>"
		- Parameters:
			- customer_id (optional): ID of customer to access, if empty, access logged in customer
		- Returns:
			- Customer Profile Details (JSON)
- Sellers:
	- PUT /api/seller/register: Register a new seller
		- Parameters:
			- Seller Details (Representative Name, Company, etc.)
			- Seller Address(es)
			- Seller Contact(s)
			- Seller Profile Image (optional)
			- Seller Account Password (plaintext, over HTTPS, stored in DB as hash+salt)

### RDBMS Schema:
- Entities:
	- User
		- Name
		- Username
		- E-Mail Address (optional)
		- Profile Image (optional)
		- Password
		- ID
		- Contact
	- Customer (IS A User)
		- Date of Registration
		- Shipping Address (multi-valued)
		- Payment Mode (composite) (multi-valued)
			- Type
			- Details
	- Seller (IS A User)
		- Company Name
		- Contact (multi-valued)
	- Item
		- Name
		- Type
		- Category (multi-valued)
		- Description
		- Features (composite, multi-valued)
			- Key
			- Value
- Relationships:
	- _Item_ OFFERED BY / ASSOCIATED WITH _Seller_
		- Quantity
		- Expected Price
	- _Customer_ GIVES RATING TO _Seller_
		- Rating
		- Feedback
	- _Customer_ ADDS _Item_ PROVIDED BY _Seller_ TO CART
		- Quantity
	- _Customer_ PURCHASES _Item_ PROVIDED BY _Seller_ FOR ORDER
		- Order ID
		- Shipping Address
- Relations
	- Customer
		-
	- Seller
		-
	- Item
		-
	- Cart
		-
	- Order
		-
	- Transactions
		-
	- User
		-
	- Customer_Addresses
		-
	- Item_Associations
		-
	- Item_Categories
		-
	- Item_Assigned_Categories
		-
	- Item_Feature_Keys
		-
	- Item_Assigned_Feature_Keys
		-