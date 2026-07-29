import pandas as pd
import psycopg2
from psycopg2 import extras

# ----------------------------
# 1. Load CSV
# ----------------------------
file_path = "data/raw/sales_data.csv"
df = pd.read_csv(file_path)

# Optional: ensure correct data types
df["order_date"] = pd.to_datetime(df["order_date"])

print(f"Loaded {len(df)} rows from CSV")

# ----------------------------
# 2. Connect to PostgreSQL
# ----------------------------
conn = psycopg2.connect(
    host="localhost",
    database="sales_db",
    user="postgres",
    password="pgadmin123"   # replace this
)

cursor = conn.cursor()

# ----------------------------
# 3. Create table (if not exists)
# ----------------------------
create_table_query = """
CREATE TABLE IF NOT EXISTS sales_orders (
    order_date DATE,
    customer_name TEXT,
    product_name TEXT,
    quantity INT,
    unit_price NUMERIC,
    total_amount NUMERIC,
    region TEXT
);
"""

cursor.execute(create_table_query)
conn.commit()

# ----------------------------
# 4. Insert data (bulk insert)
# ----------------------------
insert_query = """
INSERT INTO sales_orders (
    order_date, customer_name, product_name,
    quantity, unit_price, total_amount, region
)
VALUES %s
"""

data_tuples = list(df.itertuples(index=False, name=None))

extras.execute_values(
    cursor, insert_query, data_tuples
)

conn.commit()

# ----------------------------
# 5. Close connection
# ----------------------------
cursor.close()
conn.close()

print("Data successfully loaded into PostgreSQL 🚀")