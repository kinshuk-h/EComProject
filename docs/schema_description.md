# Schema Description (for RDBMS)

The following schema is proposed for the project, for use with an RDBMS software.

## Entities:
- User
    - Name
    - Username (unique)
    - E-Mail Address (optional) (unique)
    - Profile Image (optional)
    - Password (composite)
        - Hash
        - Salt
    - ID (primary)
    - Contact
- Customer (IS A User)
    - Date of Registration
    - Shipping Address (composite) (multi-valued)
        - Label (unique)
        - Description
    - Payment Mode (composite) (multi-valued)
        - Label (unique)
        - Type
        - Details
- Seller (IS A User)
    - Company Name
    - Business Contact (multi-valued)
- Item
    - Name
    - Type
    - Category (multi-valued)
    - Description
    - Features (multi-valued) (composite)
        - Key
        - Value

## Relationships:
(Note: Nested bullets denote relationship-specific attributes)
- _Item_ OFFERED BY / ASSOCIATED WITH _Seller_ **M:N**
    - Quantity
    - Expected Price
- _Customer_ GIVES RATING TO _Seller_ **M:N**
    - Rating
    - Feedback
- _Customer_ ADDS _Item_ PROVIDED BY _Seller_ TO CART **M:N:P**
    - Quantity
- _Customer_ PURCHASES _Item_ PROVIDED BY _Seller_ FOR ORDER **M:N:P**
    - Order ID
    - Shipping Address Label
    - Payment Mode Label
    - Date of Shipment
## Relations
- User
    Column/Attribute | Type | Properties | Remarks
    ---|---|---|---
    id | INTEGER | PRIMARY KEY AUTOINCREMENT | -
    username | VARCHAR(100) | UNIQUE | -
    email | VARCHAR(255) | UNIQUE | -
- Customer
- Seller
- Item
- Cart
- Order
- Transactions
- User
- Customer_Addresses
- Customer_Payment_Modes
- Item_Associations
- Item_Categories
- Item_Assigned_Categories
- Item_Feature_Keys
- Item_Assigned_Feature_Keys