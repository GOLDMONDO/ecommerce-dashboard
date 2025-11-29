import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import make_interp_spline
import numpy as np

# Style settings
plt.style.use("seaborn-v0_8")

# Load and prepare data
df = pd.read_csv("sales_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# === 1. Total Sales by Day (with a smooth line and high peak values) ===
plt.figure(figsize=(12, 6))

# Group sales by day
daily_sales = df.groupby('Date')['Total'].sum().reset_index()

# Convert dates to number to interpolate
x = np.arange(len(daily_sales))
y = daily_sales['Total']

# Interpolation to smooth the line
x_smooth = np.linspace(x.min(), x.max(), 300)
spl = make_interp_spline(x, y, k=3)
y_smooth = spl(x_smooth)

# Graph smooth line
plt.plot(x_smooth, y_smooth, color='b', linewidth=2)

# Mark only the high peaks (values ​​> average + 1 standard deviation)
mean_val = y.mean()
std_val = y.std()
high_peaks = y > (mean_val + std_val)

for i, (date, total) in enumerate(zip(daily_sales['Date'], daily_sales['Total'])):
    if high_peaks.iloc[i]:
        plt.text(i, total, f'${total:,.0f}', ha='center', va='bottom', fontsize=9, color='red')

# Show only one date every 7 days (every week)
xticks_indices = np.arange(0, len(daily_sales), 7)  # every 7 days
xticks_labels = daily_sales['Date'].iloc[xticks_indices].dt.strftime('%Y-%m-%d')

plt.xticks(xticks_indices, xticks_labels, rotation=45, ha='right')

plt.title("Total Sales by Day")
plt.xlabel("Date")
plt.ylabel("Sales ($)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("total_sales_by_day.png")
plt.close()

# === 2. Monthly Sales (with values above each bar) ===
plt.figure(figsize=(10, 6))
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total'].sum().reset_index()
monthly_sales['Month'] = monthly_sales['Month'].astype(str)

bars = plt.bar(monthly_sales['Month'], monthly_sales['Total'], color='skyblue', edgecolor='navy', linewidth=0.5)

# Add values above each bar
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

# === 3. Top 5 Products (with values above each bar, formato $$$) ===
plt.figure(figsize=(10, 6))
top_products = df.groupby('Product')['Total'].sum().nlargest(5).reset_index()

bars = sns.barplot(data=top_products, x='Product', y='Total', palette='viridis')

# Add values above each formatted bar $X,XXX
for bar in bars.patches:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height + 100,  # +100 so that it doesn't stick to the bar
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