Lesson 02 – Relationships & Data Integrity

Date: (Write today's date)

🎯 Objective

Learn how to connect tables in a relational database and why consistent data is essential.

What We Built Today

We improved our project by connecting Products with Suppliers.

Previously:

Products

ProductID
ProductName
Category
UnitCost
UnitPrice

Now:

Products

ProductID
ProductName
Category
SupplierID
UnitCost
UnitPrice

Now every product belongs to a supplier.

Business Problem

A company wants to know:

Which supplier provides each product?
How much inventory comes from each supplier?
Which supplier supplies the most products?
Which suppliers have the highest purchase value?

Without SupplierID, we cannot answer these questions.

Database Concept Learned
Primary Key

A Primary Key uniquely identifies each record.

Example:

Products
---------
ProductID

Every product has one unique ProductID.

Foreign Key

A Foreign Key connects two tables.

Example:

Suppliers
----------
SupplierID

↓

Products
---------
SupplierID

This relationship allows us to connect products with suppliers.

Relationship Diagram
Suppliers
-----------------
SupplierID (PK)
SupplierName
Country
Category

        │
        │
        ▼

Products
-----------------
ProductID (PK)
SupplierID (FK)
ProductName
Category
UnitCost
UnitPrice
Python Concepts Learned
Reading another CSV file
suppliers_df = pd.read_csv("data/Suppliers.csv")

Purpose:

Load supplier data into memory.

Filtering Data
matching_suppliers = suppliers_df[
    suppliers_df["Category"] == category
]

Purpose:

Find suppliers that provide the same category as the product.

Selecting Random Data
supplier_id = random.choice(
    matching_suppliers["SupplierID"].tolist()
)

Purpose:

Assign one supplier to the product.

Error Handling

Instead of allowing Python to fail unexpectedly, we checked:

if matching_suppliers.empty:
    raise ValueError(...)

This produces a meaningful error message.

Real Problem We Solved

We received this error:

ValueError:
No supplier found for category: Office

Later:

No supplier found for category: Storage

Why?

Because the product categories and supplier categories did not match exactly.

Example:

❌ Wrong

Products:
Office

Suppliers:
Office Supplies

Python sees these as different values.

Business Lesson

This is called Data Integrity.

A database works correctly only when related data is consistent.

Incorrect:

Office
Office Supplies
OFFICE
office

Correct:

Office Supplies

One standard name should be used everywhere.

Why This Matters

Imagine a company has sales reports grouped by category.

If categories are inconsistent:

Office
Office Supplies
office

The report will incorrectly show three different categories instead of one.

Python Functions Used Today
pd.read_csv()

random.choice()

tolist()

raise ValueError()
Files We Modified
products.py
Suppliers.csv
Products.csv
Interview Question

Q: What is a Foreign Key?

Answer:

A Foreign Key is a column in one table that references the Primary Key of another table. It creates a relationship between the two tables and helps maintain data integrity.

Mini Quiz
Question 1

What is the difference between a Primary Key and a Foreign Key?

Question 2

Why did we add SupplierID to the Products table?

Question 3

Why did the program produce:

No supplier found for category: Storage
Question 4

What does this code do?

matching_suppliers = suppliers_df[
    suppliers_df["Category"] == category
]
Question 5

Why is data consistency important in a database?

My Personal Notes

(Write these in your own words.)

Example:

Today I learned how two tables are connected using a Foreign Key. I also learned that even small differences in text values, such as "Office" and "Office Supplies", can break relationships between tables. This showed me why maintaining consistent master data is important in real business systems.

⭐ Today's Achievement

Today was one of the most important days in this project.

You didn't just fix a Python error—you learned a core database concept used in every ERP system:

✅ Relationships between tables
✅ Primary Keys and Foreign Keys
✅ Data integrity
✅ Validating data before using it
✅ Thinking like a data engineer, not just a programmer

These concepts are fundamental to SQL, data analytics, and supply chain systems, and you'll use them repeatedly as we continue building your project.