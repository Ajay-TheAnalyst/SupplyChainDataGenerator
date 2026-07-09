import random
from datetime import datetime, timedelta

import pandas as pd

from config.config import (
    RANDOM_SEED,
    NUM_PURCHASE_ORDERS,
    NUM_WAREHOUSES
)


def generate_purchase_orders():

    random.seed(RANDOM_SEED)

    suppliers_df = pd.read_csv("data/Suppliers.csv")

    purchase_orders = []

    start_date = datetime(2025, 1, 1)

    statuses = [
        "Pending",
        "Shipped",
        "Delivered",
        "Cancelled"
    ]

    for po_id in range(100001, 100001 + NUM_PURCHASE_ORDERS):

        supplier_id = random.choice(
            suppliers_df["SupplierID"].tolist()
        )

        warehouse_id = random.randint(
            1,
            NUM_WAREHOUSES
        )

        order_date = (
            start_date +
            timedelta(days=random.randint(0, 180))
        )

        expected_delivery = (
            order_date +
            timedelta(days=random.randint(5, 25))
        )

        status = random.choices(
            statuses,
            weights=[10, 20, 65, 5],
            k=1
        )[0]

        purchase_orders.append([
            po_id,
            supplier_id,
            warehouse_id,
            order_date.strftime("%Y-%m-%d"),
            expected_delivery.strftime("%Y-%m-%d"),
            status
        ])

    df = pd.DataFrame(
        purchase_orders,
        columns=[
            "PurchaseOrderID",
            "SupplierID",
            "WarehouseID",
            "OrderDate",
            "ExpectedDeliveryDate",
            "Status"
        ]
    )

    df.to_csv(
        "data/Purchase_Orders.csv",
        index=False
    )

    print(
        f"✅ Purchase_Orders.csv created ({len(df)} rows)"
    )