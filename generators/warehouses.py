import pandas as pd
from faker import Faker
import random

def generate_warehouses():

    fake = Faker("en_IN")

    warehouses = []

    warehouse_names = [
        "North Distribution Center",
        "South Distribution Center",
        "East Distribution Center",
        "West Distribution Center",
        "Central Distribution Center"
    ]

    capacities = [50000, 60000, 70000, 80000, 100000]

    for warehouse_id in range(1, 6):

        warehouses.append([
            warehouse_id,
            warehouse_names[warehouse_id-1],
            fake.city(),
            fake.state(),
            capacities[warehouse_id-1],
            fake.name()
        ])

    df = pd.DataFrame(
        warehouses,
        columns=[
            "WarehouseID",
            "WarehouseName",
            "City",
            "State",
            "Capacity",
            "Manager"
        ]
    )

    df.to_csv("data/Warehouses.csv", index=False)

    print("✅ Warehouses.csv created")