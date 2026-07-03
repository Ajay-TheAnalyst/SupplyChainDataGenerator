import pandas as pd
import random

def generate_products():

    random.seed(42)

    products = []

    categories = [
        "Electronics",
        "Office Supplies",
        "Furniture",
        "Networking",
        "Accessories"
    ]

    for product_id in range(1, 101):

        category = random.choice(categories)

        cost = round(random.uniform(10, 500), 2)

        price = round(cost * random.uniform(1.2, 1.8), 2)

        products.append([
            product_id,
            f"Product {product_id}",
            category,
            cost,
            price
        ])

    df = pd.DataFrame(
        products,
        columns=[
            "ProductID",
            "ProductName",
            "Category",
            "UnitCost",
            "UnitPrice"
        ]
    )

    df.to_csv("data/Products.csv", index=False)

    print("✅ Products.csv created")