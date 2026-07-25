import pandas as pd
from validators.duplicate_validator import validate_data


def check_nulls(df, table_name):
    missing_values = df.isnull().sum()

    if (missing_values > 0).any():

        print(f"❌ Missing values found in {table_name}")
        print(missing_values[missing_values > 0])
        print()

    else:

        print(f"✅ No missing values in {table_name}")


def run_null_validation():
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

    check_nulls(customers_df, "Customers")
    check_nulls(inventory_df, "Inventory")
    check_nulls(inventory_transactions_df, "Inventory_Transactions")
    check_nulls(order_items_df, "Order_Items")
    check_nulls(orders_df, "Orders")
    check_nulls(products_df, "Products")
    check_nulls(purchase_orders_items_df, "Purchase_Order_Items")
    check_nulls(purchase_orders_df, "Purchase_Orders")
    check_nulls(returns_df, "Returns")
    check_nulls(suppliers_df, "Suppliers")
    check_nulls(warehouses_df, "Warehouses")
