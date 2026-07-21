import random
from datetime import datetime, timedelta

import pandas as pd

from config.config import (
    NUM_WAREHOUSES,
    RANDOM_SEED,
    MAX_STOCK_PER_PRODUCT
)


def generate_inventory():

    random.seed(RANDOM_SEED)

    inventory_id = 1

    # Read Products.csv
    products_df = pd.read_csv("data/Products.csv")

    inventory = []

    start_date = datetime(2025, 1, 1)

    # Every warehouse stores every product
    for warehouse_id in range(1, NUM_WAREHOUSES + 1):

        for product_id in products_df["ProductID"]:

            current_stock = random.randint(0, MAX_STOCK_PER_PRODUCT)

            reorder_level = random.randint(50, 200)

            safety_stock = int(reorder_level * 0.5)

            last_restocked = (
                start_date +
                timedelta(days=random.randint(0, 180))
            ).strftime("%Y-%m-%d")

            inventory.append([
                inventory_id,
                warehouse_id,
                product_id,
                current_stock,
                reorder_level,
                safety_stock,
                last_restocked
            ])

            # Increase InventoryID for the next row
            inventory_id += 1

    df = pd.DataFrame(
        inventory,
        columns=[
            "InventoryID",
            "WarehouseID",
            "ProductID",
            "CurrentStock",
            "ReorderLevel",
            "SafetyStock",
            "LastRestocked"
        ]
    )

    df.to_csv(
        "data/Inventory.csv",
        index=False
    )

    print(f"✅ Inventory.csv created ({len(df)} rows)")