import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import make_interp_spline
import numpy as np

# Configuración de estilo
plt.style.use("seaborn-v0_8")

# Cargar y preparar datos
df = pd.read_csv("sales_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# === 1. Total Sales by Day (con línea suave y valores en picos altos) ===
plt.figure(figsize=(12, 6))

# Agrupar ventas por día
daily_sales = df.groupby('Date')['Total'].sum().reset_index()

# Convertir fechas a número para interpolar
x = np.arange(len(daily_sales))
y = daily_sales['Total']

# Interpolación para suavizar la línea
x_smooth = np.linspace(x.min(), x.max(), 300)
spl = make_interp_spline(x, y, k=3)
y_smooth = spl(x_smooth)

# Graficar línea suave
plt.plot(x_smooth, y_smooth, color='b', linewidth=2)

# Marcar solo los picos altos (valores > promedio + 1 desviación estándar)
mean_val = y.mean()
std_val = y.std()
high_peaks = y > (mean_val + std_val)

for i, (date, total) in enumerate(zip(daily_sales['Date'], daily_sales['Total'])):
    if high_peaks.iloc[i]:
        plt.text(i, total, f'${total:,.0f}', ha='center', va='bottom', fontsize=9, color='red')

# Mostrar solo una fecha cada 7 días (cada semana)
xticks_indices = np.arange(0, len(daily_sales), 7)  # cada 7 días
xticks_labels = daily_sales['Date'].iloc[xticks_indices].dt.strftime('%Y-%m-%d')

plt.xticks(xticks_indices, xticks_labels, rotation=45, ha='right')

plt.title("Total Sales by Day")
plt.xlabel("Date")
plt.ylabel("Sales ($)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("total_sales_by_day.png")
plt.close()

# === 2. Monthly Sales (con valores encima de cada barra) ===
plt.figure(figsize=(10, 6))
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total'].sum().reset_index()
monthly_sales['Month'] = monthly_sales['Month'].astype(str)

bars = plt.bar(monthly_sales['Month'], monthly_sales['Total'], color='skyblue', edgecolor='navy', linewidth=0.5)

# Añadir valores encima de cada barra
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height,
             f'${height:,.0f}',
             ha='center', va='bottom', fontsize=10, color='black')

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.close()

# === 3. Top 5 Products (con valores encima de cada barra, formato $$$) ===
plt.figure(figsize=(10, 6))
top_products = df.groupby('Product')['Total'].sum().nlargest(5).reset_index()

bars = sns.barplot(data=top_products, x='Product', y='Total', palette='viridis')

# Añadir valores encima de cada barra con formato $X,XXX
for bar in bars.patches:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height + 100,  # +100 para que no quede pegado a la barra
             f'${height:,.0f}',
             ha='center', va='bottom', fontsize=10, color='black', fontweight='bold')

plt.title("Top 5 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_products.png")
plt.close()

print("✅ Charts generated successfully:")
print("- total_sales_by_day.png")
print("- monthly_sales.png")
print("- top_products.png")