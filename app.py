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
    background-color:#F7F9FC;
}

h1,h2,h3{
    color:#003366;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:12px;
    padding:18px;
    box-shadow:0px 3px 8px rgba(0,0,0,0.15);
}

section[data-testid="stSidebar"]{
    background:#F1F3F6;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# TITLE
# ----------------------------------------------------------

st.title("🛒 E-Commerce Sales Analysis & Business Intelligence Dashboard")

st.write("""
This dashboard provides interactive business insights using
Python, Streamlit, Plotly, Machine Learning and Business
Intelligence techniques.
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
# MACHINE LEARNING MODEL
# ----------------------------------------------------------

X = df[
    [
        "Quantity",
        "Price",
        "CostPrice",
        "Discount"
    ]
]

y = df["FinalAmount"]

model = LinearRegression()

model.fit(X, y)

# ----------------------------------------------------------
# SIDEBAR FILTERS
# ----------------------------------------------------------

st.sidebar.header("Dashboard Filters")

country = st.sidebar.multiselect(
    "Country",
    sorted(df["Country"].unique()),
    default=sorted(df["Country"].unique())
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
    (df["Country"].isin(country)) &
    (df["Category"].isin(category)) &
    (df["PaymentMethod"].isin(payment))
]

st.sidebar.markdown("---")
st.sidebar.success(f"Records : {len(filtered_df)}")
# ----------------------------------------------------------
# KPI CALCULATIONS
# ----------------------------------------------------------

total_revenue = filtered_df["FinalAmount"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["OrderID"].nunique()
total_customers = filtered_df["CustomerID"].nunique()
total_products = filtered_df["ProductID"].nunique()

# ----------------------------------------------------------
# KPI SECTION
# ----------------------------------------------------------

st.subheader("📊 Business Overview")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "💰 Total Revenue",
    f"${total_revenue:,.2f}"
)

col2.metric(
    "📈 Total Profit",
    f"${total_profit:,.2f}"
)

col3.metric(
    "🛍 Orders",
    total_orders
)

col4.metric(
    "👥 Customers",
    total_customers
)

col5.metric(
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
    xaxis_title="Month",
    yaxis_title="Revenue",
    template="plotly_white"
)

st.plotly_chart(
    fig_month,
    use_container_width=True
)

# ----------------------------------------------------------
# CATEGORY SALES
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
# COUNTRY SALES
# ----------------------------------------------------------

country_sales = (
    filtered_df
    .groupby("Country")["FinalAmount"]
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

fig_country.update_layout(
    template="plotly_white"
)

st.plotly_chart(
    fig_country,
    use_container_width=True
)
# ----------------------------------------------------------
# TOP 10 CUSTOMERS
# ----------------------------------------------------------

st.markdown("---")
st.subheader("👥 Top Customers")

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

st.subheader("📦 Top Products")

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

payment_analysis = (
    filtered_df.groupby("PaymentMethod")["FinalAmount"]
    .sum()
    .reset_index()
)

fig_payment = px.pie(
    payment_analysis,
    names="PaymentMethod",
    values="FinalAmount",
    hole=0.45,
    title="Revenue by Payment Method"
)

st.plotly_chart(fig_payment, use_container_width=True)

# ----------------------------------------------------------
# REGION ANALYSIS
# ----------------------------------------------------------

st.subheader("🌍 Region-wise Revenue")

region_sales = (
    filtered_df.groupby("Region")["FinalAmount"]
    .sum()
    .reset_index()
)

fig_region = px.treemap(
    region_sales,
    path=["Region"],
    values="FinalAmount",
    color="FinalAmount",
    title="Regional Revenue Distribution"
)

st.plotly_chart(fig_region, use_container_width=True)

# ----------------------------------------------------------
# REVENUE CATEGORY DISTRIBUTION
# ----------------------------------------------------------

st.subheader("📊 Revenue Category")

revenue_category = (
    filtered_df["RevenueCategory"]
    .value_counts()
    .reset_index()
)

revenue_category.columns = [
    "RevenueCategory",
    "Count"
]

fig_revenue = px.bar(
    revenue_category,
    x="RevenueCategory",
    y="Count",
    color="RevenueCategory",
    text_auto=True,
    title="Revenue Category Distribution"
)

fig_revenue.update_layout(template="plotly_white")

st.plotly_chart(fig_revenue, use_container_width=True)

# ----------------------------------------------------------
# CORRELATION HEATMAP
# ----------------------------------------------------------

st.markdown("---")
st.subheader("🔥 Correlation Heatmap")

correlation = filtered_df[
    [
        "Quantity",
        "Price",
        "CostPrice",
        "Discount",
        "TotalSales",
        "Profit",
        "FinalAmount"
    ]
].corr()

fig_heatmap = px.imshow(
    correlation,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    title="Feature Correlation Matrix"
)

st.plotly_chart(fig_heatmap, use_container_width=True)
# ----------------------------------------------------------
# MACHINE LEARNING SALES PREDICTION
# ----------------------------------------------------------

st.markdown("---")
st.header("🤖 Sales Prediction")

st.write("Enter the values below to predict the Final Sales Amount.")

col1, col2 = st.columns(2)

with col1:

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        max_value=100,
        value=5
    )

    price = st.number_input(
        "Price",
        min_value=1.0,
        value=500.0
    )

with col2:

    cost_price = st.number_input(
        "Cost Price",
        min_value=1.0,
        value=300.0
    )

    discount = st.slider(
        "Discount",
        0.0,
        0.50,
        0.10,
        0.01
    )

if st.button("Predict Sales"):

    input_data = np.array([
        [
            quantity,
            price,
            cost_price,
            discount
        ]
    ])

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
    "Number of Rows",
    5,
    100,
    10
)

st.dataframe(
    filtered_df.head(rows),
    use_container_width=True
)

# ----------------------------------------------------------
# SUMMARY STATISTICS
# ----------------------------------------------------------

st.markdown("---")
st.header("📈 Summary Statistics")

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

highest_country = (
    filtered_df.groupby("Country")["FinalAmount"]
    .sum()
    .idxmax()
)

highest_customer = (
    filtered_df.groupby("CustomerName")["FinalAmount"]
    .sum()
    .idxmax()
)

highest_product = (
    filtered_df.groupby("ProductName")["FinalAmount"]
    .sum()
    .idxmax()
)

highest_payment = (
    filtered_df.groupby("PaymentMethod")["FinalAmount"]
    .sum()
    .idxmax()
)

st.info(f"""

Highest Revenue Category : **{highest_category}**

Highest Revenue Country : **{highest_country}**

Best Customer : **{highest_customer}**

Best Selling Product : **{highest_product}**

Most Preferred Payment Method : **{highest_payment}**

""")

# ----------------------------------------------------------
# DATA INFORMATION
# ----------------------------------------------------------

st.markdown("---")
st.header("🗂 Dataset Information")

info = pd.DataFrame({

    "Column Name": filtered_df.columns,

    "Data Type": filtered_df.dtypes.astype(str)

})

st.dataframe(
    info,
    use_container_width=True
)
# ----------------------------------------------------------
# ABOUT PROJECT
# ----------------------------------------------------------

st.markdown("---")
st.header("📖 About Project")

st.write("""
This E-Commerce Sales Analysis and Business Intelligence Dashboard
demonstrates a complete data analytics workflow using Python,
Pandas, Plotly, Streamlit, Scikit-learn, and Power BI concepts.

The project analyzes customer behavior, product performance,
sales trends, payment analysis, profitability, and predicts
future sales using a Linear Regression model.
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
    "Machine Learning Prediction",
    "Business Intelligence Dashboard"
]

for obj in objectives:
    st.write(f"✅ {obj}")

# ----------------------------------------------------------
# TOOLS & TECHNOLOGIES
# ----------------------------------------------------------

st.markdown("---")
st.header("🛠 Tools & Technologies")

tools = pd.DataFrame({

    "Technology":[
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

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric(
        "Revenue",
        f"${total_revenue:,.2f}"
    )

with c2:
    st.metric(
        "Profit",
        f"${total_profit:,.2f}"
    )

with c3:
    st.metric(
        "Orders",
        total_orders
    )

with c4:
    st.metric(
        "Customers",
        total_customers
    )

with c5:
    st.metric(
        "Products",
        total_products
    )

# ----------------------------------------------------------
# PROJECT CONCLUSION
# ----------------------------------------------------------

st.markdown("---")
st.header("📝 Conclusion")

st.success("""
The dashboard provides a comprehensive overview of business
performance through interactive visualizations and predictive
analytics.

It enables decision-makers to monitor sales, evaluate customer
behavior, identify high-performing products, analyze payment
methods, understand profitability, and forecast future sales
using machine learning.

This project demonstrates a complete end-to-end Business
Intelligence and Data Analytics solution.
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

<b>Python | Streamlit | Plotly | Pandas | Scikit-learn | Power BI</b>

<br><br>

© 2026 Mini Project

</div>
""",
unsafe_allow_html=True
)

# ----------------------------------------------------------
# END OF APPLICATION
# ----------------------------------------------------------
