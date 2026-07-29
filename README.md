# 📦 Supply Chain Data Generator & Validation Framework

A Python-based Supply Chain Data Generator that creates realistic business datasets and validates them using a complete data quality framework.

The project simulates a real-world supply chain system by generating interconnected datasets such as Customers, Products, Orders, Inventory, Suppliers, Purchase Orders, and Returns.

Before the data is used for analysis, multiple validation checks ensure the integrity and quality of the generated data.## Features

- Generate realistic supply chain datasets
- Create relational data across multiple tables
- Duplicate validation
- Null value validation
- Foreign key validation
- Business rule validation
- Automated validation report## Project Structure

```text
SupplyChainDataGenerator
│
├── config/
├── data/
├── generators/
├── validators/
│   ├── duplicate_validator.py
│   ├── null_validator.py
│   ├── foreign_key_validator.py
│   ├── business_rule_validator.py
│   └── validation_report.py
│
├── main.py
└── README.md
```
| Table                  | Description                |
| ---------------------- | -------------------------- |
| Customers              | Customer information       |
| Products               | Product catalog            |
| Suppliers              | Supplier information       |
| Warehouses             | Warehouse details          |
| Orders                 | Customer orders            |
| Order_Items            | Products inside each order |
| Inventory              | Warehouse stock            |
| Inventory_Transactions | Inventory movement         |
| Purchase_Orders        | Supplier purchase orders   |
| Purchase_Order_Items   | Items purchased            |
| Returns                | Returned products          |

## Validation Framework

The project validates data using multiple quality checks.

### Duplicate Validation

- CustomerID
- ProductID
- OrderID
- SupplierID
- WarehouseID
- InventoryID
- TransactionID
- PurchaseOrderID
- PurchaseOrderItemID
- ReturnID

### Null Validation

Checks every dataset for missing values.

### Foreign Key Validation

- Orders → Customers
- Order_Items → Orders
- Order_Items → Products
- Inventory → Products
- Inventory → Warehouses
- Purchase_Orders → Suppliers
- Purchase_Order_Items → Purchase_Orders
- Purchase_Order_Items → Products
- Returns → Orders
- Returns → Customers
- Returns → Products

### Business Rule Validation

- UnitCost > 0
- UnitPrice > 0
- Quantity > 0
- ReturnedQuantity > 0
- RefundAmount > 0
- ReturnedQuantity ≤ OrderedQuantity
- RefundAmount = ReturnedQuantity × UnitPrice

## Technologies Used

- Python
- Pandas
- Faker
- NumPy
- CSV
- Git
- GitHub

Upcoming:

- MySQL
- SQL
- Power BI

## How to Run

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install pandas faker numpy
```

Run

```bash
python main.py
```

## Sample Validation Report

```text
C:\Users\hp\PycharmProjects\SupplyChainDataGenerator\.venv\Scripts\python.exe C:\Users\hp\PycharmProjects\SupplyChainDataGenerator\main.py 
====================================
 Supply Chain Data Generator 
====================================
✅ ReturnedQuantity validation passed
✅ RefundAmount validation passed

=================================================================
               SUPPLY CHAIN VALIDATION REPORT
=================================================================
Duplicate           CustomerID                                        PASS    Issues: 0
Duplicate           InventoryID                                       PASS    Issues: 0
Duplicate           TransactionID                                     PASS    Issues: 0
Duplicate           OrderItemID                                       PASS    Issues: 0
Duplicate           OrderID                                           PASS    Issues: 0
Duplicate           ProductID                                         PASS    Issues: 0
Duplicate           PurchaseOrderItemID                               PASS    Issues: 0
Duplicate           PurchaseOrderID                                   PASS    Issues: 0
Duplicate           ReturnID                                          PASS    Issues: 0
Duplicate           SupplierID                                        PASS    Issues: 0
Duplicate           WarehouseID                                       PASS    Issues: 0
Null                Customers                                         PASS    Issues: 0
Null                Inventory                                         PASS    Issues: 0
Null                Inventory_Transactions                            PASS    Issues: 0
Null                Order_Items                                       PASS    Issues: 0
Null                Orders                                            PASS    Issues: 0
Null                Products                                          PASS    Issues: 0
Null                Purchase_Order_Items                              PASS    Issues: 0
Null                Purchase_Orders                                   PASS    Issues: 0
Null                Returns                                           PASS    Issues: 0
Null                Suppliers                                         PASS    Issues: 0
Null                Warehouses                                        PASS    Issues: 0
Foreign Key         Orders -> Customers                               PASS    Issues: 0
Foreign Key         Order_items -> Orders                             PASS    Issues: 0
Foreign Key         Order_Items -> Products                           PASS    Issues: 0
Foreign Key         Inventory -> Products                             PASS    Issues: 0
Foreign Key         Inventory -> Warehouses                           PASS    Issues: 0
Foreign Key         Purchase_Orders -> Suppliers                      PASS    Issues: 0
Foreign Key         Returns -> Orders                                 PASS    Issues: 0
Foreign Key         Returns -> Customers                              PASS    Issues: 0
Foreign Key         Returns -> Products                               PASS    Issues: 0
Foreign Key         Purchase_Order_Items -> Purchase_Orders           PASS    Issues: 0
Foreign Key         Purchase_Order_Items -> Products                  PASS    Issues: 0
Business Rule       Products.UnitCost                                 PASS    Issues: 0
Business Rule       Products.UnitPrice                                PASS    Issues: 0
Business Rule       Order_Items.Quantity                              PASS    Issues: 0
Business Rule       Order_Items.UnitPrice                             PASS    Issues: 0
Business Rule       Purchase_Order_Items.Quantity                     PASS    Issues: 0
Business Rule       Purchase_Order_Items.UnitCost                     PASS    Issues: 0
Business Rule       Returns.ReturnedQuantity                          PASS    Issues: 0
Business Rule       Returns.RefundAmount                              PASS    Issues: 0
=================================================================
Overall Status : ✅ PASS
=================================================================
====================================
All datasets generated successfully!
====================================

Process finished with exit code 0

```


## Future Improvements

- Store generated data in MySQL
- Build analytical SQL queries
- Develop interactive Power BI dashboards
- Add automated unit tests
- Export validation reports to Excel or PDF

## Author

Ajay Kumar

Google Data Analytics Professional Certificate

Data Analytics Portfolio Project