from validators.validation_report import add_result
import pandas as pd
from validators.null_validator import validate_data




def check_foreign_key(
        child_df,
        child_column,
        parent_df,
        parent_column,
        relationship_name
):

    invalid_rows = child_df[
        ~child_df[child_column].isin(parent_df[parent_column])
    ]

    if len(invalid_rows) > 0:

        print(f"❌ Foreign Key Error Found in {relationship_name}")
        print(invalid_rows)
        print()

    else:

        add_result(
            "Foreign Key",
            relationship_name,
            "PASS",
            0
        )


def run_foreign_key_validation():
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

    check_foreign_key(
        orders_df,
        "CustomerID",
        customers_df,
        "CustomerID",
        "Orders -> Customers"
    )
    check_foreign_key(
        order_items_df,
        "OrderID",
        orders_df,
        "OrderID",
        "Order_items -> Orders"
    )

    check_foreign_key(
        order_items_df,
        "ProductID",
        products_df,
        "ProductID",
        "Order_Items -> Products"
    )

    check_foreign_key(
        inventory_df,
        "ProductID",
        products_df,
        "ProductID",
        "Inventory -> Products"
    )

    check_foreign_key(
        inventory_df,
        "WarehouseID",
        warehouses_df,
        "WarehouseID",
        "Inventory -> Warehouses"
    )

    check_foreign_key(
        purchase_orders_df,
        "SupplierID",
        suppliers_df,
        "SupplierID",
        "Purchase_Orders -> Suppliers"
    )

    check_foreign_key(
        returns_df,
        "OrderID",
        orders_df,
        "OrderID",
        "Returns -> Orders"
    )

    check_foreign_key(
        returns_df,
        "CustomerID",
        customers_df,
        "CustomerID",
        "Returns -> Customers"
    )

    check_foreign_key(
        returns_df,
        "ProductID",
        products_df,
        "ProductID",
        "Returns -> Products"
    )

    check_foreign_key(
        purchase_orders_items_df,
        "PurchaseOrderID",
        purchase_orders_df,
        "PurchaseOrderID",
        "Purchase_Order_Items -> Purchase_Orders"
    )

    check_foreign_key(
        purchase_orders_items_df,
        "ProductID",
        products_df,
        "ProductID",
        "Purchase_Order_Items -> Products"
    )