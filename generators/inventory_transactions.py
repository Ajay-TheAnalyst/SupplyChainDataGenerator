import random
from datetime import datetime, timedelta

import pandas as pd

from config.config import (
    RANDOM_SEED,
    NUM_WAREHOUSES,
    NUM_INVENTORY_TRANSACTIONS
)


def generate_inventory_transactions():

    random.seed(RANDOM_SEED)

    products_df = pd.read_csv("data/Products.csv")

    transactions = []

    start_date = datetime(2025, 1, 1)

    transaction_types = [
        "IN",
        "OUT",
        "RETURN",
        "ADJUSTMENT"
    ]

    for transaction_id in range(1, NUM_INVENTORY_TRANSACTIONS + 1):

        warehouse_id = random.randint(1, NUM_WAREHOUSES)

        product_id = random.choice(
            products_df["ProductID"].tolist()
        )

        transaction_type = random.choices(
            transaction_types,
            weights=[25, 60, 10, 5],
            k=1
        )[0]

        quantity = random.randint(1, 100)

        transaction_date = (
            start_date +
            timedelta(days=random.randint(0, 180))
        ).strftime("%Y-%m-%d")

        transactions.append([
            transaction_id,
            warehouse_id,
            product_id,
            transaction_type,
            quantity,
            transaction_date
        ])

    df = pd.DataFrame(
        transactions,
        columns=[
            "TransactionID",
            "WarehouseID",
            "ProductID",
            "TransactionType",
            "Quantity",
            "TransactionDate"
        ]
    )

    df.to_csv(
        "data/Inventory_Transactions.csv",
        index=False
    )

    print(f"✅ Inventory_Transactions.csv created ({len(df)} rows)")