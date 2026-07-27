import pandas as pd
from validators.duplicate_validator import validate_data


def check_positive(df, column_name, table_name):

    invalid_rows = df[
        df[column_name] <= 0
    ]

    if len(invalid_rows) > 0:
        print(f"❌ Invalid {column_name} value found in {table_name}")
        print(invalid_rows)
        print()

    else:
        print(f"✅ No invalid {column_name} values found in {table_name}")


def run_check_positive():
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

    check_positive(products_df,"UnitCost","Products")
    check_positive(products_df,"UnitPrice","Products")
    check_positive(order_items_df,"Quantity","Order_Items")
    check_positive(order_items_df,"UnitPrice","Order_Items")
    check_positive(purchase_orders_items_df,"Quantity","Purchase_Order_Items")
    check_positive(purchase_orders_items_df,"UnitCost","Purchase_Order_Items")
    check_positive(returns_df,"ReturnedQuantity","Returns")
    check_positive(returns_df,"RefundAmount","Returns")
