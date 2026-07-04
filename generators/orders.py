import random
from datetime import datetime, timedelta

import pandas as pd

from config.config import (
    NUM_CUSTOMERS,
    NUM_WAREHOUSES,
    NUM_ORDERS,
    RANDOM_SEED
)


def generate_orders():

    random.seed(RANDOM_SEED)

    statuses = [
        "Delivered",
        "Shipped",
        "Processing",
        "Cancelled"
    ]

    priorities = [
        "Low",
        "Medium",
        "High"
    ]

    payment_methods = [
        "Credit Card",
        "UPI",
        "Bank Transfer",
        "Cash on Delivery"
    ]

    start_date = datetime(2024, 1, 1)

    orders = []

    for order_id in range(100001, 100001 + NUM_ORDERS):

        order_date = start_date + timedelta(
            days=random.randint(0, 730)
        )

        orders.append([
            order_id,
            random.randint(1, NUM_CUSTOMERS),
            random.randint(1, NUM_WAREHOUSES),
            order_date.strftime("%Y-%m-%d"),
            random.choice(statuses),
            random.choice(priorities),
            random.choice(payment_methods)
        ])

    df = pd.DataFrame(
        orders,
        columns=[
            "OrderID",
            "CustomerID",
            "WarehouseID",
            "OrderDate",
            "Status",
            "Priority",
            "PaymentMethod"
        ]
    )

    df.to_csv("data/Orders.csv", index=False)

    print(f"✅ Orders.csv created ({len(df)} rows)")