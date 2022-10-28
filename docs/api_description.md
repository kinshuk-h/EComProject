# API Description

The following API endpoints are provided, categorized as follows:

### [Authentication](api/auth.md):
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

### [Customers](api/customer.md):
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

### [Sellers](api/seller.md):
- PUT /api/seller/register: Register a new seller
    - Parameters:
        - Seller Details (Representative Name, Company, etc.)
        - Seller Address(es)
        - Seller Contact(s)
        - Seller Profile Image (optional)
        - Seller Account Password (plaintext, over HTTPS, stored in DB as hash+salt)