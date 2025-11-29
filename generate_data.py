import pandas as pd
import random
from datetime import datetime, timedelta
import numpy as np

# Seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define product catalog with weights (popularity) and price ranges
products = {
    "Laptop": {"weight": 1, "price_range": (800, 1500)},
    "Monitor": {"weight": 2, "price_range": (150, 400)},
    "Keyboard": {"weight": 5, "price_range": (20, 80)},
    "Mouse": {"weight": 6, "price_range": (10, 50)},
    "Headphones": {"weight": 4, "price_range": (30, 150)},
    "Webcam": {"weight": 3, "price_range": (25, 100)},
    "USB Cable": {"weight": 8, "price_range": (5, 20)},
    "External SSD": {"weight": 2, "price_range": (60, 200)},
}

product_names = list(products.keys())
weights = [products[p]["weight"] for p in product_names]

# Cities with weighted volume
cities = ["CDMX", "Guadalajara", "Monterrey", "Puebla", "Tijuana"]
city_weights = [5, 3, 4, 2, 2]  # CDMX tiene más pedidos

# Generate dates from January to December 2024 (you can extend more if you want)
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = pd.date_range(start_date, end_date, freq='D')

# Ready to collect data
data = []

# Generate ~800 orders (more realistic than 500 rows without context)
for _ in range(800):
    # Choose a date
    date = random.choice(date_range)

    # Peak season: increase probability of orders in Nov-Dec (optional)

    # Choose city and product with weights
    city = random.choices(cities, weights=city_weights)[0]
    product = random.choices(product_names, weights=weights)[0]

    # Base price
    min_p, max_p = products[product]["price_range"]
    base_price = round(random.uniform(min_p, max_p), 2)

    # Adjustment: expensive products tend to be sold in smaller quantities
    if base_price > 500:
        quantity = random.randint(1, 2)
    elif base_price > 100:
        quantity = random.randint(1, 3)
    else:
        quantity = random.randint(1, 8)

    total = round(base_price * quantity, 2)

    # Order status (more 'Delivered' than others)
    status = random.choices(
        ["Delivered", "Shipped", "Processing"],
        weights=[70, 20, 10]
    )[0]

    data.append({
        "Date": date,
        "Product": product,
        "Quantity": quantity,
        "Price": base_price,
        "Total": total,
        "City": city,
        "Status": status
    })

# Create DataFrame
df = pd.DataFrame(data)

# Sort by date
df = df.sort_values("Date").reset_index(drop=True)

# Save

df.to_csv("sales_data.csv", index=False)
print("✅ File 'sales_data.csv' generated with realistic data.")
print(f"   Total number of records: {len(df)}")
print(f"   Dates: {df['Date'].min()} a {df['Date'].max()}")
print(f"   Unique products: {df['Product'].nunique()}")

import os
print(f"   Save path: {os.getcwd()}")