Objective

Understand how companies purchase products from suppliers.

Business Scenario

Imagine Warehouse 2 is running out of HP laptops.

Current Stock:

HP Laptop = 12

Reorder Level:

HP Laptop = 50

The purchasing department creates a Purchase Order.

Supplier
      │
      ▼
Purchase Order
      │
      ▼
Warehouse
      │
      ▼
Inventory Increases
What is a Purchase Order?

A Purchase Order (PO) is an official document sent to a supplier requesting products.

Example:

PO	Supplier	Warehouse	Status
100001	Dell Supplier	Warehouse 2	Delivered
Table Structure
Column	Meaning
PurchaseOrderID	Unique PO Number
SupplierID	Supplier receiving the order
WarehouseID	Receiving warehouse
OrderDate	Date created
ExpectedDeliveryDate	Expected arrival
Status	Current status
Business Rule

One supplier can receive many purchase orders.

Supplier
   │
   ├── Purchase Order 1
   ├── Purchase Order 2
   ├── Purchase Order 3
Python Concepts Learned
datetime

Used to create dates.

from datetime import datetime
timedelta

Used to add days.

expected_delivery = order_date + timedelta(days=10)
strftime()

Converts a Python date into text.

order_date.strftime("%Y-%m-%d")
random.choices()

Unlike random.choice(), it lets us assign probabilities.

status = random.choices(
    statuses,
    weights=[10,20,65,5]
)[0]

Meaning:

Pending → 10%
Shipped → 20%
Delivered → 65%
Cancelled → 5%

This makes the generated data more realistic.

Database Relationships
Suppliers
    │
    ▼
Purchase Orders
    │
    ▼
Warehouses
Interview Question

Q: What is the difference between a Customer Order and a Purchase Order?

Answer:

A Customer Order is created when a customer buys products from the company.
A Purchase Order is created when the company buys products from a supplier.