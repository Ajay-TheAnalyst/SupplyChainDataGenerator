from validators.validation_report import add_result
import pandas as pd
from validators.duplicate_validator import validate_data


def check_positive(df, column_name, table_name):

    invalid_rows = df[
        df[column_name] <= 0
    ]

    if len(invalid_rows) > 0:

        add_result(
            "Business Rule",
            f"{table_name}.{column_name}",
            "FAIL",
            len(invalid_rows)
        )

    else:

        add_result(
            "Business Rule",
            f"{table_name}.{column_name}",
            "PASS",
            0
        )

def check_return_quantity(returns_df, order_items_df):

    merged_df = returns_df.merge(
        order_items_df,
        on=["OrderID", "ProductID"]
    )

    invalid_rows = merged_df[
        merged_df["ReturnedQuantity"] >
        merged_df["Quantity"]
    ]

    if len(invalid_rows) > 0:

        print("❌ Invalid ReturnedQuantity found in Returns")
        print(invalid_rows)
        print()

    else:

        print("✅ ReturnedQuantity validation passed")


def check_refund_amount(returns_df, order_items_df):

    merged_df = returns_df.merge(
        order_items_df,
        on=["OrderID", "ProductID"]
    )

    merged_df["ExpectedRefund"] = (
        merged_df["ReturnedQuantity"] *
        merged_df["UnitPrice"]
    )

    invalid_rows = merged_df[
        merged_df["RefundAmount"] !=
        merged_df["ExpectedRefund"]
    ]

    if len(invalid_rows) > 0:

        print("❌ Invalid RefundAmount found in Returns")
        print(invalid_rows)
        print()

    else:

        print("✅ RefundAmount validation passed")


#def check_order_dates(orders_df):

    #invalid_rows = orders_df[
       # orders_df["OrderDate"] >
        #orders_df["ShipDate"]
    #]

    #if len(invalid_rows) > 0:

        #print("❌ Invalid OrderDate / ShipDate found")
        #print(invalid_rows)
        #print()

    #else:

        #print("✅ OrderDate validation passed")


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

    # Positive value validations
    check_positive(products_df, "UnitCost", "Products")
    check_positive(products_df, "UnitPrice", "Products")

    check_positive(order_items_df, "Quantity", "Order_Items")
    check_positive(order_items_df, "UnitPrice", "Order_Items")

    check_positive(
        purchase_orders_items_df,
        "Quantity",
        "Purchase_Order_Items"
    )

    check_positive(
        purchase_orders_items_df,
        "UnitCost",
        "Purchase_Order_Items"
    )

    check_positive(
        returns_df,
        "ReturnedQuantity",
        "Returns"
    )

    check_positive(
        returns_df,
        "RefundAmount",
        "Returns"
    )

    # Advanced Business Rules
    check_return_quantity(
        returns_df,
        order_items_df
    )

    check_refund_amount(
        returns_df,
        order_items_df
    )

    #check_order_dates(
       # orders_df
    #)