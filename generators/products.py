import random
import pandas as pd

from config.config import NUM_PRODUCTS, RANDOM_SEED
from master_data.product_catalog import PRODUCT_CATALOG


PRICE_RULES = {
    "Laptop": (650, 1400),
    "Monitor": (120, 450),
    "Mouse": (25, 90),
    "Keyboard": (30, 120),
    "Webcam": (40, 150),
    "Dock": (80, 250),
    "SSD": (60, 220),
    "Switch": (180, 1500),
    "Printer": (150, 500),
    "Chair": (150, 500),
    "Desk": (200, 700),
    "Office Supplies": (2, 25)
}


def generate_products():

    random.seed(RANDOM_SEED)

    # Read Suppliers.csv
    suppliers_df = pd.read_csv("data/Suppliers.csv")

    products = []

    for product_id in range(1, NUM_PRODUCTS + 1):

        brand, model, product_type, category = random.choice(PRODUCT_CATALOG)

        if product_type not in PRICE_RULES:
            raise ValueError(
                f"No price rule defined for {product_type}"
            )

        # Find suppliers that supply this category
        matching_suppliers = suppliers_df[
            suppliers_df["Category"] == category
            ]

        if matching_suppliers.empty:
            raise ValueError(
                f"No supplier found for category: {category}"
            )

        supplier_id = random.choice(
            matching_suppliers["SupplierID"].tolist()
        )

        min_price, max_price = PRICE_RULES[product_type]

        unit_price = random.randint(min_price, max_price)

        unit_cost = round(unit_price * random.uniform(0.6, 0.8), 2)

        product_name = f"{brand} {model}"

        products.append([
            product_id,
            product_name,
            brand,
            category,
            supplier_id,
            unit_cost,
            unit_price
        ])

    df = pd.DataFrame(
        products,
        columns=[
            "ProductID",
            "ProductName",
            "Brand",
            "Category",
            "SupplierID",
            "UnitCost",
            "UnitPrice"
        ]
    )

    df.to_csv("data/Products.csv", index=False)

    print(f"✅ Products.csv created ({len(df)} rows)")