import random
import pandas as pd

from config.config import (
    NUM_ORDERS,
    MAX_ITEMS_PER_ORDER,
    RANDOM_SEED
)


def generate_order_items():

    random.seed(RANDOM_SEED)

    # Read Products.csv
    products_df = pd.read_csv("data/Products.csv")

    # Create ProductID -> UnitPrice dictionary
    price_lookup = dict(
        zip(
            products_df["ProductID"],
            products_df["UnitPrice"]
        )
    )

    # Create ProductID -> UnitCost dictionary
    cost_lookup = dict(
        zip(
            products_df["ProductID"],
            products_df["UnitCost"]
        )
    )

    order_items = []

    order_item_id = 1



    # Every order gets 1-5 products
    for order_id in range(100001, 100001 + NUM_ORDERS):

        number_of_items = random.randint(1, MAX_ITEMS_PER_ORDER)

        # Prevent duplicate products in the same order
        selected_products = random.sample(
            products_df["ProductID"].tolist(),
            number_of_items
        )

        for product_id in selected_products:

            quantity = random.randint(1, 10)

            unit_price = price_lookup[product_id]

            discount = random.choice(
                [0, 5, 10, 15]
            )

            order_items.append([
                order_item_id,
                order_id,
                product_id,
                quantity,
                unit_price,
                discount
            ])

            order_item_id += 1

    df = pd.DataFrame(
        order_items,
        columns=[
            "OrderItemID",
            "OrderID",
            "ProductID",
            "Quantity",
            "UnitPrice",
            "Discount"
        ]
    )

    df.to_csv(
        "data/Order_Items.csv",
        index=False
    )

    print(f"✅ Order_Items.csv created ({len(df)} rows)")