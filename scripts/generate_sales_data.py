import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Make results reproducible
np.random.seed(42)

customers = [
    "Deloitte", "KPMG", "PwC", "EY", "HSBC",
    "Barclays", "Google", "Microsoft", "Amazon",
    "Accenture", "Infosys", "TCS"
]

products = [
    "AI Platform",
    "Cloud Suite",
    "Analytics Dashboard",
    "Data Warehouse",
    "CRM Software"
]

regions = [
    "London",
    "Manchester",
    "Birmingham",
    "Leeds",
    "Edinburgh"
]

num_records = 10000

start_date = datetime(2024, 1, 1)

data = []

for i in range(num_records):

    order_date = start_date + timedelta(
        days=np.random.randint(0, 730)
    )

    customer = np.random.choice(customers)
    product = np.random.choice(products)

    quantity = np.random.randint(1, 10)

    unit_price = np.random.randint(500, 5000)

    total_amount = quantity * unit_price

    region = np.random.choice(regions)

    data.append([
        order_date.date(),
        customer,
        product,
        quantity,
        unit_price,
        total_amount,
        region
    ])

df = pd.DataFrame(
    data,
    columns=[
        "order_date",
        "customer_name",
        "product_name",
        "quantity",
        "unit_price",
        "total_amount",
        "region"
    ]
)

df.to_csv(
    "data/raw/sales_data.csv",
    index=False
)

print("Dataset generated successfully!")
print(df.head())