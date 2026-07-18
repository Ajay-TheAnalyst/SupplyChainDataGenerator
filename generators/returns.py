import pandas as pd
import random

RETURN_REASONS = [
    "Product Condition Not Good",
    "Color Mismatch",
    "Different Product Received",
    "Changed with Another Product"
]

RETURN_STATUS = [
    "Pending",
    "Approved",
    "Rejected",
    "Refunded"
]


def generate_returns():
    orders_df = pd.read_csv("data/Orders.csv")
    order_items_df = pd.read_csv("data/Order_Items.csv")

    return_items = []
    return_id = 1

    for index, row in orders_df.iterrows():
        order_id = row["OrderID"]
        customer_id = row["CustomerID"]

        random_num = random.randint(1, 100)

        if random_num <= 6:
            current_orders = order_items_df[
                order_items_df["OrderID"] == order_id
            ]

            product_ids = current_orders["ProductID"].tolist()
            num_products = random.randint(1, len(product_ids))
            selected_products = random.sample(product_ids, num_products)

            for product_id in selected_products:
                matching_products = current_orders[
                    current_orders["ProductID"] == product_id
                ]

                ordered_quantity = matching_products.iloc[0]["Quantity"]
                returned_quantity = random.randint(1, ordered_quantity)

                reason = random.choice(RETURN_REASONS)
                status = random.choice(RETURN_STATUS)

                unit_price = matching_products.iloc[0]["UnitPrice"]
                refund_amount = returned_quantity * unit_price

                return_items.append({
                    "ReturnID": return_id,
                    "OrderID": order_id,
                    "CustomerID": customer_id,
                    "ProductID": product_id,
                    "ReturnedQuantity": returned_quantity,
                    "Reason": reason,
                    "Status": status,
                    "RefundAmount": refund_amount
                })

                return_id += 1

    returns_df = pd.DataFrame(return_items)
    returns_df.to_csv("data/Returns.csv", index=False)

    print("✅ Returns.csv generated successfully!")