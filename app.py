# ==========================================================
# E-Commerce Sales Analysis & Business Intelligence Dashboard
# Streamlit Application
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from sklearn.linear_model import LinearRegression

# ----------------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------------

st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------------

st.markdown("""
<style>

.main{
    background:#F8F9FA;
}

h1,h2,h3,h4{
    color:#0A3D62;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:12px;
    padding:18px;
    box-shadow:0 2px 8px rgba(0,0,0,0.15);
}

section[data-testid="stSidebar"]{
    background:#EEF2F7;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# TITLE
# ----------------------------------------------------------

st.title("🛒 E-Commerce Sales Analysis & Business Intelligence Dashboard")

st.write("""
Interactive dashboard for analyzing customer behavior,
product performance, regional sales, profitability,
payment methods, and sales prediction.
""")

# ----------------------------------------------------------
# LOAD DATA
# ----------------------------------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv("final_merged_dataset.csv")

    df["OrderDate"] = pd.to_datetime(df["OrderDate"])

    return df


df = load_data()

# ----------------------------------------------------------
# TRAIN MACHINE LEARNING MODEL
# ----------------------------------------------------------

X = df[["Quantity","Price","CostPrice","Discount"]]

y = df["FinalAmount"]

model = LinearRegression()

model.fit(X,y)

# ----------------------------------------------------------
# SIDEBAR FILTERS
# ----------------------------------------------------------

st.sidebar.header("Dashboard Filters")

region = st.sidebar.multiselect(
    "Region",
    sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

category = st.sidebar.multiselect(
    "Category",
    sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

payment = st.sidebar.multiselect(
    "Payment Method",
    sorted(df["PaymentMethod"].unique()),
    default=sorted(df["PaymentMethod"].unique())
)

filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["PaymentMethod"].isin(payment))
]

st.sidebar.markdown("---")

st.sidebar.success(
    f"Filtered Records : {len(filtered_df)}"
)
# ----------------------------------------------------------
# KPI CALCULATIONS
# ----------------------------------------------------------

total_revenue = filtered_df["FinalAmount"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["OrderID"].nunique()
total_customers = filtered_df["CustomerID"].nunique()
total_products = filtered_df["ProductID"].nunique()

# ----------------------------------------------------------
# KPI DASHBOARD
# ----------------------------------------------------------

st.subheader("📊 Business Overview")

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

with kpi1:
    st.metric(
        "💰 Revenue",
        f"${total_revenue:,.2f}"
    )

with kpi2:
    st.metric(
        "📈 Profit",
        f"${total_profit:,.2f}"
    )

with kpi3:
    st.metric(
        "🛒 Orders",
        total_orders
    )

with kpi4:
    st.metric(
        "👥 Customers",
        total_customers
    )

with kpi5:
    st.metric(
        "📦 Products",
        total_products
    )

st.markdown("---")

# ----------------------------------------------------------
# MONTHLY SALES TREND
# ----------------------------------------------------------

monthly_sales = (
    filtered_df
    .groupby(filtered_df["OrderDate"].dt.to_period("M"))
    ["FinalAmount"]
    .sum()
    .reset_index()
)

monthly_sales["OrderDate"] = monthly_sales["OrderDate"].astype(str)

fig_month = px.line(
    monthly_sales,
    x="OrderDate",
    y="FinalAmount",
    markers=True,
    title="Monthly Sales Trend"
)

fig_month.update_layout(
    template="plotly_white",
    xaxis_title="Month",
    yaxis_title="Revenue"
)

st.plotly_chart(
    fig_month,
    use_container_width=True
)

# ----------------------------------------------------------
# REVENUE BY CATEGORY
# ----------------------------------------------------------

category_sales = (
    filtered_df
    .groupby("Category")["FinalAmount"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig_category = px.bar(
    category_sales,
    x="Category",
    y="FinalAmount",
    color="FinalAmount",
    text_auto=".2s",
    title="Revenue by Category"
)

fig_category.update_layout(
    template="plotly_white"
)

st.plotly_chart(
    fig_category,
    use_container_width=True
)

# ----------------------------------------------------------
# REGION-WISE REVENUE
# ----------------------------------------------------------

region_sales = (
    filtered_df
    .groupby("Region")["FinalAmount"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig_region = px.bar(
    region_sales,
    x="Region",
    y="FinalAmount",
    color="FinalAmount",
    text_auto=".2s",
    title="Region-wise Revenue"
)

fig_region.update_layout(
    template="plotly_white"
)

st.plotly_chart(
    fig_region,
    use_container_width=True
)

# ----------------------------------------------------------
# PROFIT BY CATEGORY
# ----------------------------------------------------------

profit_category = (
    filtered_df
    .groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig_profit = px.bar(
    profit_category,
    x="Category",
    y="Profit",
    color="Profit",
    text_auto=".2s",
    title="Profit by Category"
)

fig_profit.update_layout(
    template="plotly_white"
)

st.plotly_chart(
    fig_profit,
    use_container_width=True
)
# ----------------------------------------------------------
# TOP 10 CUSTOMERS
# ----------------------------------------------------------

st.markdown("---")
st.subheader("👥 Top 10 Customers")

top_customers = (
    filtered_df.groupby("CustomerName")["FinalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_customer = px.bar(
    top_customers,
    x="CustomerName",
    y="FinalAmount",
    color="FinalAmount",
    text_auto=".2s",
    title="Top 10 Customers by Revenue"
)

fig_customer.update_layout(
    template="plotly_white",
    xaxis_title="Customer",
    yaxis_title="Revenue"
)

st.plotly_chart(fig_customer, use_container_width=True)

# ----------------------------------------------------------
# TOP 10 PRODUCTS
# ----------------------------------------------------------

st.markdown("---")
st.subheader("📦 Top 10 Products")

top_products = (
    filtered_df.groupby("ProductName")["FinalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_product = px.bar(
    top_products,
    x="ProductName",
    y="FinalAmount",
    color="FinalAmount",
    text_auto=".2s",
    title="Top 10 Products by Revenue"
)

fig_product.update_layout(
    template="plotly_white",
    xaxis_title="Product",
    yaxis_title="Revenue"
)

st.plotly_chart(fig_product, use_container_width=True)

# ----------------------------------------------------------
# PAYMENT METHOD ANALYSIS
# ----------------------------------------------------------

st.markdown("---")
st.subheader("💳 Payment Method Analysis")

payment_sales = (
    filtered_df.groupby("PaymentMethod")["FinalAmount"]
    .sum()
    .reset_index()
)

fig_payment = px.pie(
    payment_sales,
    names="PaymentMethod",
    values="FinalAmount",
    hole=0.45,
    title="Revenue by Payment Method"
)

st.plotly_chart(fig_payment, use_container_width=True)

# ----------------------------------------------------------
# PAYMENT STATUS ANALYSIS
# ----------------------------------------------------------

payment_status = (
    filtered_df.groupby("PaymentStatus")["OrderID"]
    .count()
    .reset_index()
)

payment_status.columns = [
    "PaymentStatus",
    "Orders"
]

fig_status = px.bar(
    payment_status,
    x="PaymentStatus",
    y="Orders",
    color="PaymentStatus",
    text_auto=True,
    title="Payment Status Distribution"
)

fig_status.update_layout(template="plotly_white")

st.plotly_chart(fig_status, use_container_width=True)

# ----------------------------------------------------------
# COUNTRY-WISE SALES
# ----------------------------------------------------------

country_sales = (
    filtered_df.groupby("Country")["FinalAmount"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig_country = px.bar(
    country_sales,
    x="Country",
    y="FinalAmount",
    color="FinalAmount",
    text_auto=".2s",
    title="Country-wise Revenue"
)

fig_country.update_layout(template="plotly_white")

st.plotly_chart(fig_country, use_container_width=True)

# ----------------------------------------------------------
# CORRELATION HEATMAP
# ----------------------------------------------------------

st.markdown("---")
st.subheader("🔥 Correlation Heatmap")

corr = filtered_df[
    [
        "Quantity",
        "Price",
        "CostPrice",
        "Discount",
        "TotalSales",
        "FinalAmount",
        "Profit"
    ]
].corr()

fig_heatmap = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    title="Correlation Matrix"
)

st.plotly_chart(fig_heatmap, use_container_width=True)
# ----------------------------------------------------------
# MACHINE LEARNING SALES PREDICTION
# ----------------------------------------------------------

st.markdown("---")
st.header("🤖 Sales Prediction")

st.write("Enter product details to predict the Final Sales Amount.")

col1, col2 = st.columns(2)

with col1:

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        max_value=100,
        value=5
    )

    price = st.number_input(
        "Price ($)",
        min_value=1.0,
        value=500.0
    )

with col2:

    cost_price = st.number_input(
        "Cost Price ($)",
        min_value=1.0,
        value=300.0
    )

    discount = st.slider(
        "Discount",
        min_value=0.00,
        max_value=0.50,
        value=0.10,
        step=0.01
    )

if st.button("Predict Sales Amount"):

    input_data = np.array(
        [[quantity, price, cost_price, discount]]
    )

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Final Sales Amount : ${prediction[0]:,.2f}"
    )

# ----------------------------------------------------------
# DATASET EXPLORER
# ----------------------------------------------------------

st.markdown("---")
st.header("📋 Dataset Explorer")

rows = st.slider(
    "Select Number of Rows",
    min_value=5,
    max_value=100,
    value=10
)

st.dataframe(
    filtered_df.head(rows),
    use_container_width=True
)

# ----------------------------------------------------------
# SUMMARY STATISTICS
# ----------------------------------------------------------

st.markdown("---")
st.header("📈 Statistical Summary")

st.dataframe(
    filtered_df.describe(),
    use_container_width=True
)

# ----------------------------------------------------------
# DOWNLOAD FILTERED DATASET
# ----------------------------------------------------------

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered Dataset",
    data=csv,
    file_name="filtered_dataset.csv",
    mime="text/csv"
)

# ----------------------------------------------------------
# BUSINESS INSIGHTS
# ----------------------------------------------------------

st.markdown("---")
st.header("💡 Business Insights")

highest_category = (
    filtered_df.groupby("Category")["FinalAmount"]
    .sum()
    .idxmax()
)

highest_region = (
    filtered_df.groupby("Region")["FinalAmount"]
    .sum()
    .idxmax()
)

highest_country = (
    filtered_df.groupby("Country")["FinalAmount"]
    .sum()
    .idxmax()
)

best_product = (
    filtered_df.groupby("ProductName")["FinalAmount"]
    .sum()
    .idxmax()
)

best_customer = (
    filtered_df.groupby("CustomerName")["FinalAmount"]
    .sum()
    .idxmax()
)

st.info(f"""
📌 Highest Revenue Category : **{highest_category}**

🌍 Highest Revenue Region : **{highest_region}**

🏆 Highest Revenue Country : **{highest_country}**

📦 Best Selling Product : **{best_product}**

👤 Top Customer : **{best_customer}**
""")

# ----------------------------------------------------------
# DATASET INFORMATION
# ----------------------------------------------------------

st.markdown("---")
st.header("🗂 Dataset Information")

info_df = pd.DataFrame({
    "Column": filtered_df.columns,
    "Data Type": filtered_df.dtypes.astype(str)
})

st.dataframe(
    info_df,
    use_container_width=True
)
# ----------------------------------------------------------
# ABOUT PROJECT
# ----------------------------------------------------------

st.markdown("---")
st.header("📖 About Project")

st.write("""
The E-Commerce Sales Analysis and Business Intelligence Dashboard
is a complete end-to-end data analytics project developed using
Python, Streamlit, Pandas, Plotly, Scikit-learn and Power BI.

The application enables users to analyze sales performance,
customer behavior, product performance, regional revenue,
payment trends and profitability through interactive
visualizations and business intelligence techniques.
""")

# ----------------------------------------------------------
# PROJECT OBJECTIVES
# ----------------------------------------------------------

st.markdown("---")
st.header("🎯 Project Objectives")

objectives = [
    "Customer Behavior Analysis",
    "Product Performance Analysis",
    "Sales Trend Analysis",
    "Profitability Analysis",
    "Regional Performance Analysis",
    "Payment Method Analysis",
    "Business Intelligence Dashboard",
    "Sales Prediction using Machine Learning"
]

for objective in objectives:
    st.write(f"✔ {objective}")

# ----------------------------------------------------------
# TOOLS & TECHNOLOGIES
# ----------------------------------------------------------

st.markdown("---")
st.header("🛠 Tools & Technologies")

tools = pd.DataFrame({
    "Technology": [
        "Python",
        "Pandas",
        "NumPy",
        "Plotly",
        "Streamlit",
        "Scikit-learn",
        "Power BI",
        "Jupyter Notebook"
    ]
})

st.dataframe(
    tools,
    use_container_width=True,
    hide_index=True
)

# ----------------------------------------------------------
# FINAL KPI SUMMARY
# ----------------------------------------------------------

st.markdown("---")
st.header("📊 Dashboard Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Revenue", f"${total_revenue:,.2f}")

with col2:
    st.metric("Total Profit", f"${total_profit:,.2f}")

with col3:
    st.metric("Total Orders", total_orders)

col4, col5 = st.columns(2)

with col4:
    st.metric("Total Customers", total_customers)

with col5:
    st.metric("Total Products", total_products)

# ----------------------------------------------------------
# CONCLUSION
# ----------------------------------------------------------

st.markdown("---")
st.header("📝 Conclusion")

st.success("""
This dashboard demonstrates a complete Business Intelligence
solution for E-Commerce Sales Analysis.

Key capabilities include:

• Interactive KPI Dashboard

• Customer Analysis

• Product Performance Analysis

• Sales Trend Analysis

• Profitability Analysis

• Regional Sales Analysis

• Payment Analysis

• Machine Learning Sales Prediction

The dashboard supports data-driven decision-making through
interactive visualizations and predictive analytics.
""")

# ----------------------------------------------------------
# FOOTER
# ----------------------------------------------------------

st.markdown("---")

st.markdown(
"""
<div style="text-align:center">

<h3>E-Commerce Sales Analysis & Business Intelligence Dashboard</h3>

Built using

<b>Python | Streamlit | Pandas | Plotly | Scikit-learn | Power BI</b>

<br><br>

© 2026 Mini Project

</div>
""",
unsafe_allow_html=True
)

# ----------------------------------------------------------
# END OF APPLICATION
# ----------------------------------------------------------
