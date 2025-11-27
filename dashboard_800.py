import streamlit as st
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

    # === 2. Ventas diarias (agrupadas) ===
    st.subheader("📈 Ventas Diarias (Agrupadas)")
    daily_sales = filtered_df.groupby('Date')['Total'].sum().reset_index()
    fig1 = px.line(daily_sales, x='Date', y='Total', title="Ventas Totales por Día")
    st.plotly_chart(fig1, use_container_width=True)

    # === 3. Ventas mensuales (opcional pero útil) ===
    st.subheader("📆 Ventas por Mes")
    filtered_df['YearMonth'] = filtered_df['Date'].dt.to_period('M').astype(str)
    monthly_sales = filtered_df.groupby('YearMonth')['Total'].sum().reset_index()
    fig2 = px.bar(monthly_sales, x='YearMonth', y='Total', title="Ventas por Mes")
    st.plotly_chart(fig2, use_container_width=True)

    # === 4. Top 5 productos más vendidos (por ingresos) ===
    st.subheader("🏆 Top 5 Productos por Ingresos")
    top_products = filtered_df.groupby('Product')['Total'].sum().nlargest(5).reset_index()
    fig3 = px.bar(top_products, x='Product', y='Total', title="Ingresos por Producto (Top 5)")
    st.plotly_chart(fig3, use_container_width=True)

    # === 5. Ventas por ciudad ===
    st.subheader("📍 Ventas por Ciudad")
    sales_by_city = filtered_df.groupby('City')['Total'].sum().reset_index()
    fig4 = px.pie(sales_by_city, values='Total', names='City', title="Distribución de Ventas por Ciudad")
    st.plotly_chart(fig4, use_container_width=True)

    # === 6. Tabla de datos (opcional) ===
    with st.expander("Ver datos filtrados"):
        st.dataframe(filtered_df)
