import pandas as pd
from faker import Faker
import random

def generate_suppliers():

    fake = Faker()

    random.seed(42)
    Faker.seed(42)

    countries = [
        "India",
        "China",
        "Vietnam",
        "Germany",
        "USA",
        "Japan",
        "South Korea",
        "Malaysia"
    ]

    categories = [
        "Electronics",
        "Office Supplies",
        "Furniture",
        "Networking",
        "Accessories"
    ]

    payment_terms = [
        "Net 30",
        "Net 45",
        "Net 60"
    ]

    suppliers = []

    for supplier_id in range(1, 81):      # 80 suppliers

        suppliers.append([
            supplier_id,
            fake.company(),
            random.choice(countries),
            random.choice(categories),
            random.randint(5,30),          # Lead Time
            round(random.uniform(3.5,5.0),2),
            random.choice(payment_terms),
            fake.company_email()
        ])

    df = pd.DataFrame(
        suppliers,
        columns=[
            "SupplierID",
            "SupplierName",
            "Country",
            "Category",
            "LeadTimeDays",
            "SupplierRating",
            "PaymentTerms",
            "Email"
        ]
    )

    df.to_csv("data/Suppliers.csv", index=False)

    print("✅ Suppliers.csv created")