import pandas as pd
import random
from datetime import datetime, timedelta
import numpy as np

# Semilla para reproducibilidad
random.seed(42)
np.random.seed(42)

# Definir catálogo de productos con pesos (popularidad) y rangos de precio
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

# Ciudades con volumen ponderado
cities = ["CDMX", "Guadalajara", "Monterrey", "Puebla", "Tijuana"]
city_weights = [5, 3, 4, 2, 2]  # CDMX tiene más pedidos

# Generar fechas desde enero a octubre 2024 (puedes extender a nov-dic si quieres)
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = pd.date_range(start_date, end_date, freq='D')

# Lista para acumular datos
data = []

# Generar ~800 órdenes (más realista que 500 filas sin contexto)
for _ in range(800):
    # Elegir fecha
    date = random.choice(date_range)

    # Temporada alta: incrementar probabilidad de pedidos en nov-dic (opcional)
    # En este caso solo hasta octubre, pero si quieres extender, avísame.

    # Elegir ciudad y producto con pesos
    city = random.choices(cities, weights=city_weights)[0]
    product = random.choices(product_names, weights=weights)[0]

    # Precio base
    min_p, max_p = products[product]["price_range"]
    base_price = round(random.uniform(min_p, max_p), 2)

    # Ajuste: productos caros suelen venderse en menor cantidad
    if base_price > 500:
        quantity = random.randint(1, 2)
    elif base_price > 100:
        quantity = random.randint(1, 3)
    else:
        quantity = random.randint(1, 8)

    total = round(base_price * quantity, 2)

    # Estado del pedido (más 'Delivered' que otros)
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

# Crear DataFrame
df = pd.DataFrame(data)

# Ordenar por fecha
df = df.sort_values("Date").reset_index(drop=True)

# Guardar
df.to_csv("sales_data_800.csv", index=False)
print("✅ Archivo 'sales_data_800.csv' generado con datos realistas.")
print(f"   Total de registros: {len(df)}")
print(f"   Fechas: {df['Date'].min()} a {df['Date'].max()}")
print(f"   Productos únicos: {df['Product'].nunique()}")