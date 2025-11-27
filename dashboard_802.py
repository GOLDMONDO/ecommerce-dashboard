import streamlit as st  # Importación necesaria al principio
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="E-commerce Insights", layout="wide")

# Título
st.title("📊 Operational Insights Dashboard")
st.markdown("Análisis de ventas para una tienda de e-commerce (datos simulados)")

# Cargar y preparar datos
df = pd.read_csv("sales_data_800.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Sidebar: filtros
st.sidebar.header("Filtros")
cities = st.sidebar.multiselect("Selecciona ciudades", df['City'].unique(), default=df['City'].unique())
products = st.sidebar.multiselect("Selecciona productos", df['Product'].unique(), default=df['Product'].unique())

# Aplicar filtros
filtered_df = df[(df['City'].isin(cities)) & (df['Product'].isin(products))]

if filtered_df.empty:
    st.warning("No hay datos con los filtros seleccionados.")
else:
    # === 1. Métricas clave ===
    total_sales = filtered_df['Total'].sum()
    total_orders = len(filtered_df)
    avg_order_value = total_sales / total_orders

    col1, col2, col3 = st.columns(3)
    col1.metric("Ventas Totales", f"${total_sales:,.2f}")
    col2.metric("Número de Pedidos", f"{total_orders:,}")
    col3.metric("Ticket Promedio", f"${avg_order_value:,.2f}")

    # === 2. Ventas diarias (agrupadas) - CORREGIDO ===
    st.subheader("📈 Ventas Diarias (Agrupadas)")

    # Agrupar ventas por día (solo días con ventas)
    daily_sales_raw = filtered_df.groupby('Date')['Total'].sum().reset_index()

    # Crear un rango de fechas completo para el año 2024
    # Esto asegura que el eje X muestre todo el año, incluso meses sin ventas
    date_range = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')

    # Crear un DataFrame con el rango de fechas completo
    daily_sales_complete = pd.DataFrame({'Date': date_range})

    # Unir con los datos reales de ventas diarias, rellenando con 0 donde no hay ventas
    # Esto es crucial para que el gráfico muestre las fechas vacías
    daily_sales = daily_sales_complete.merge(daily_sales_raw, on='Date', how='left').fillna(0)

    # Generar el gráfico con el DataFrame que incluye todas las fechas
    fig1 = px.line(daily_sales, x='Date', y='Total', title="Ventas Totales por Día")
    st.plotly_chart(fig1, width='stretch')

    # === 3. Ventas mensuales (opcional pero útil) ===
    st.subheader("📆 Ventas por Mes")
    # Asegurar que YearMonth sea string para la visualización
    filtered_df['YearMonth'] = filtered_df['Date'].dt.to_period('M').astype(str)
    # Agrupar ventas por mes
    monthly_sales_raw = filtered_df.groupby('YearMonth')['Total'].sum().reset_index()
    # Usamos directamente la agrupación (mostrará solo meses con datos)
    monthly_sales = monthly_sales_raw

    fig2 = px.bar(monthly_sales, x='YearMonth', y='Total', title="Ventas por Mes")
    st.plotly_chart(fig2, width='stretch')

    # === 4. Top 5 productos más vendidos (por ingresos) ===
    st.subheader("🏆 Top 5 Productos por Ingresos")
    top_products = filtered_df.groupby('Product')['Total'].sum().nlargest(5).reset_index()
    fig3 = px.bar(top_products, x='Product', y='Total', title="Ingresos por Producto (Top 5)")
    st.plotly_chart(fig3, width='stretch')

    # === 5. Ventas por ciudad ===
    st.subheader("📍 Ventas por Ciudad")
    sales_by_city = filtered_df.groupby('City')['Total'].sum().reset_index()
    fig4 = px.pie(sales_by_city, values='Total', names='City', title="Distribución de Ventas por Ciudad")
    st.plotly_chart(fig4, width='stretch')

    # === 6. Tabla de datos (opcional) ===
    with st.expander("Ver datos filtrados"):
        st.dataframe(filtered_df)