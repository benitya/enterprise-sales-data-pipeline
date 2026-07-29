CREATE TABLE sales_orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE,
    customer_name VARCHAR(100),
    product_name VARCHAR(100),
    quantity INT,
    unit_price NUMERIC(10,2),
    total_amount NUMERIC(10,2),
    region VARCHAR(50)
);