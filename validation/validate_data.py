import pandas as pd


def validate_data():
    customers_df = pd.read_csv("data/Customers.csv")
    inventory_df = pd.read_csv("data/Inventory.csv")
    inventory_transactions_df = pd.read_csv("data/Inventory_Transactions.csv")
    order_items_df = pd.read_csv("data/Order_Items.csv")
    orders_df = pd.read_csv("data/Orders.csv")
    products_df = pd.read_csv("data/Products.csv")
    purchase_orders_items_df = pd.read_csv("data/Purchase_Order_Items.csv")
    purchase_orders_df = pd.read_csv("data/Purchase_Orders.csv")
    returns_df = pd.read_csv("data/Returns.csv")
    suppliers_df = pd.read_csv("data/Suppliers.csv")
    warehouses_df = pd.read_csv("data/Warehouses.csv")

    return (
        customers_df,
        inventory_df,
        inventory_transactions_df,
        order_items_df,
        orders_df,
        products_df,
        purchase_orders_items_df,
        purchase_orders_df,
        returns_df,
        suppliers_df,
        warehouses_df
    )



def check_duplicates(df, column_name):

    if df[column_name].duplicated().any():

        print(f"Duplicate {column_name} Found")

    else:

        print(f"No Duplicates {column_name} Found")


customers_df, \
inventory_df, \
inventory_transactions_df, \
order_items_df, \
orders_df, \
products_df, \
purchase_orders_items_df, \
purchase_orders_df, \
returns_df, \
suppliers_df, \
warehouses_df = validate_data()

check_duplicates(customers_df,"CustomerID")
check_duplicates(inventory_df, "WarehouseID")
check_duplicates(inventory_transactions_df, "TransactionID")
check_duplicates(order_items_df, "OrderItemID")
check_duplicates(orders_df, "OrderID")
check_duplicates(products_df, "ProductID")
check_duplicates(purchase_orders_items_df, "PurchaseOrderItemID")
check_duplicates(purchase_orders_df, "PurchaseOrderID")
check_duplicates(returns_df, "ReturnID")
check_duplicates(suppliers_df, "SupplierID")
check_duplicates(warehouses_df, "WarehouseID")











