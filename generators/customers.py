import pandas as pd
from faker import Faker
import random

def generate_customers():

    fake = Faker("en_IN")

    random.seed(42)
    Faker.seed(42)

    customers = []

    customer_types = [
        "Retail",
        "Wholesale",
        "Corporate"
    ]

    for customer_id in range(1, 2001):

        customers.append([
            customer_id,
            fake.company(),
            fake.city(),
            fake.state(),
            random.choice(customer_types),
            fake.email()
        ])

    df = pd.DataFrame(
        customers,
        columns=[
            "CustomerID",
            "CustomerName",
            "City",
            "State",
            "CustomerType",
            "Email"
        ]
    )

    df.to_csv("data/Customers.csv", index=False)

    print("✅ Customers.csv created")