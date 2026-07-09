📚 Lesson 1 – Project Foundation

Date: (Write today's date)

🎯 Objective

Build the foundation for a Supply Chain Analytics project using Python.

What I Learned
1. Project Structure

Instead of writing all code in one file, we organize it into folders.

SupplyChainDataGenerator/
│
├── config/
├── data/
├── generators/
├── master_data/
├── main.py

Why?

Easier to maintain
Easier to debug
Professional structure
2. Python Modules

Each file has a specific job.

Example:

products.py
customers.py
orders.py
inventory.py

main.py calls each generator.

generate_products()
generate_customers()
generate_orders()
3. Functions

A function performs one specific task.

Example:

def generate_products():

Benefits:

Reusable
Easy to test
Organized code
4. Random Data Generation

We used:

random.randint()
random.choice()
random.choices()

Purpose:

Generate realistic business data.

Example:

quantity = random.randint(1,10)
5. Pandas

We learned how to create DataFrames.

df = pd.DataFrame(data)

Read CSV

pd.read_csv()

Write CSV

df.to_csv()
🏢 Supply Chain Concepts
Master Data

Data that changes very rarely.

Examples:

Products
Suppliers
Warehouses
Customers
Transaction Data

Data created during daily business operations.

Examples:

Orders
Order Items
Inventory Transactions
📌 Business Flow
Supplier
      │
      ▼
Products
      │
      ▼
Inventory
      │
      ▼
Customer Orders
🐍 Python Concepts Learned
Functions
Imports
Lists
Dictionaries
Loops
Reading CSV
Writing CSV
Random module
💡 Interview Question

Q: What is the difference between Master Data and Transaction Data?

Answer:

Master data is relatively static information used across the business, such as products, customers, suppliers, and warehouses. Transaction data records day-to-day business activities, such as orders, inventory movements, and shipments.