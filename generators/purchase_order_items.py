import random
import pandas as pd

from config.config import (
    RANDOM_SEED,
    MAX_PRODUCTS_PER_PURCHASE_ORDER
)


def generate_purchase_order_items():

    random.seed(RANDOM_SEED)

    purchase_orders_df = pd.read_csv("data/Purchase_Orders.csv")
    products_df = pd.read_csv("data/Products.csv")

    purchase_order_items = []

    purchase_order_item_id = 1

    # Loop through every Purchase Order
    for index, row in purchase_orders_df.iterrows():

        purchase_order_id = row["PurchaseOrderID"]
        supplier_id = row["SupplierID"]

        # Find products supplied by this supplier
        matching_products = products_df[
            products_df["SupplierID"] == supplier_id
        ]

        # Skip if supplier has no products
        if len(matching_products) == 0:
            continue

        # Decide how many products this PO will contain
        number_of_products = random.randint(
            1,
            min(
                MAX_PRODUCTS_PER_PURCHASE_ORDER,
                len(matching_products)
            )
        )

        # Randomly select products
        selected_products = random.sample(
            matching_products["ProductID"].tolist(),
            number_of_products
        )

        # Create one record for each selected product
        for product_id in selected_products:

            matching_product = products_df[
                products_df["ProductID"] == product_id
            ]

            unit_cost = matching_product.iloc[0]["UnitCost"]

            quantity = random.randint(20, 200)

            purchase_order_items.append([
                purchase_order_item_id,
                purchase_order_id,
                product_id,
                quantity,
                unit_cost
            ])

            purchase_order_item_id += 1

    df = pd.DataFrame(
        purchase_order_items,
        columns=[
            "PurchaseOrderItemID",
            "PurchaseOrderID",
            "ProductID",
            "Quantity",
            "UnitCost"
        ]
    )

    df.to_csv(
        "data/Purchase_Order_Items.csv",
        index=False
    )

    print(
        f"✅ Purchase_Order_Items.csv created ({len(df)} rows)"
    )