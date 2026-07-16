# ============================================================
# E-Commerce Sales Analysis and Business Intelligence Dashboard
# app.py
# Part 1
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import joblib

from sklearn.linear_model import LinearRegression

# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------

st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#F8F9FA;
}

h1,h2,h3,h4{
    color:#1F4E79;
}

[data-testid="stMetricValue"]{
    font-size:28px;
    color:#0F9D58;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:12px;
    padding:15px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.15);
}

.sidebar .sidebar-content{
    background-color:#F5F5F5;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# TITLE
# ------------------------------------------------------------

st.title("🛒 E-Commerce Sales Analysis & Business Intelligence Dashboard")

st.markdown(
"""
Interactive dashboard developed using **Streamlit, Plotly,
Pandas, Machine Learning and Business Intelligence concepts**.

Use the filters from the sidebar to explore the business data.
"""
)

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv("final_merged_dataset.csv")

    df["OrderDate"] = pd.to_datetime(df["OrderDate"])

    return df


df = load_data()

# ------------------------------------------------------------
# LOAD MODEL
# ------------------------------------------------------------

@st.cache_resource
def load_model():

    model = joblib.load("model.pkl")

    return model


model = load_model()

# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------

st.sidebar.title("Dashboard Filters")

country = st.sidebar.multiselect(
    "Select Country",
    sorted(df["Country"].unique()),
    default=sorted(df["Country"].unique())
)

category = st.sidebar.multiselect(
    "Select Category",
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
# ------------------------------------------------------------
# KPI CALCULATIONS
# ------------------------------------------------------------

total_revenue = filtered_df["FinalAmount"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["OrderID"].nunique()
total_customers = filtered_df["CustomerID"].nunique()
total_products = filtered_df["ProductID"].nunique()

# ------------------------------------------------------------
# KPI CARDS
# ------------------------------------------------------------

st.subheader("📊 Business KPIs")

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

with kpi1:
    st.metric(
        label="💰 Total Revenue",
        value=f"${total_revenue:,.2f}"
    )

with kpi2:
    st.metric(
        label="📈 Total Profit",
        value=f"${total_profit:,.2f}"
    )

with kpi3:
    st.metric(
        label="🛍 Total Orders",
        value=f"{total_orders:,}"
    )

with kpi4:
    st.metric(
        label="👥 Customers",
        value=f"{total_customers:,}"
    )

with kpi5:
    st.metric(
        label="📦 Products",
        value=f"{total_products:,}"
    )

st.markdown("---")

# ------------------------------------------------------------
# MONTHLY SALES TREND
# ------------------------------------------------------------

monthly_sales = (
    filtered_df
    .groupby(filtered_df["OrderDate"].dt.to_period("M"))["FinalAmount"]
    .sum()
    .reset_index()
)

monthly_sales["OrderDate"] = monthly_sales["OrderDate"].astype(str)

fig_month = px.line(
    monthly_sales,
    x="OrderDate",
    y="FinalAmount",
    markers=True,
    title="📅 Monthly Sales Trend"
)

fig_month.update_layout(
    xaxis_title="Month",
    yaxis_title="Revenue",
    template="plotly_white"
)

st.plotly_chart(fig_month, use_container_width=True)

# ------------------------------------------------------------
# CATEGORY SALES
# ------------------------------------------------------------

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
    title="🛒 Revenue by Category"
)

fig_category.update_layout(
    xaxis_title="Category",
    yaxis_title="Revenue",
    template="plotly_white"
)

st.plotly_chart(fig_category, use_container_width=True)

# ------------------------------------------------------------
# COUNTRY SALES
# ------------------------------------------------------------

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
    title="🌍 Country-wise Revenue"
)

fig_country.update_layout(
    xaxis_title="Country",
    yaxis_title="Revenue",
    template="plotly_white"
)

st.plotly_chart(fig_country, use_container_width=True)
# ------------------------------------------------------------
# TOP 10 CUSTOMERS
# ------------------------------------------------------------

st.markdown("---")
st.subheader("👥 Customer Analysis")

top_customers = (
    filtered_df
    .groupby("CustomerName")["FinalAmount"]
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
    title="Top 10 Customers by Revenue"
)

fig_customer.update_layout(
    xaxis_title="Customer",
    yaxis_title="Revenue",
    template="plotly_white"
)

st.plotly_chart(fig_customer, use_container_width=True)

# ------------------------------------------------------------
# TOP 10 PRODUCTS
# ------------------------------------------------------------

top_products = (
    filtered_df
    .groupby("ProductName")["FinalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_products = px.bar(
    top_products,
    x="ProductName",
    y="FinalAmount",
    color="FinalAmount",
    title="Top 10 Products by Revenue"
)

fig_products.update_layout(
    xaxis_title="Product",
    yaxis_title="Revenue",
    template="plotly_white"
)

st.plotly_chart(fig_products, use_container_width=True)

# ------------------------------------------------------------
# PAYMENT METHOD ANALYSIS
# ------------------------------------------------------------

st.markdown("---")
st.subheader("💳 Payment Method Analysis")

payment_analysis = (
    filtered_df
    .groupby("PaymentMethod")["FinalAmount"]
    .sum()
    .sort_values(ascending=False)
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

# ------------------------------------------------------------
# PAYMENT STATUS ANALYSIS
# ------------------------------------------------------------

payment_status = (
    filtered_df
    .groupby("PaymentStatus")["FinalAmount"]
    .sum()
    .reset_index()
)

fig_status = px.bar(
    payment_status,
    x="PaymentStatus",
    y="FinalAmount",
    color="PaymentStatus",
    title="Payment Status Analysis"
)

fig_status.update_layout(template="plotly_white")

st.plotly_chart(fig_status, use_container_width=True)

# ------------------------------------------------------------
# REVENUE CATEGORY DISTRIBUTION
# ------------------------------------------------------------

st.markdown("---")
st.subheader("📊 Revenue Category Distribution")

revenue_category = (
    filtered_df["RevenueCategory"]
    .value_counts()
    .reset_index()
)

revenue_category.columns = ["RevenueCategory", "Count"]

fig_revenue = px.bar(
    revenue_category,
    x="RevenueCategory",
    y="Count",
    color="RevenueCategory",
    title="Revenue Category Distribution"
)

fig_revenue.update_layout(template="plotly_white")

st.plotly_chart(fig_revenue, use_container_width=True)

# ------------------------------------------------------------
# REGION ANALYSIS
# ------------------------------------------------------------

region_sales = (
    filtered_df
    .groupby("Region")["FinalAmount"]
    .sum()
    .reset_index()
)

fig_region = px.treemap(
    region_sales,
    path=["Region"],
    values="FinalAmount",
    color="FinalAmount",
    title="Regional Revenue Analysis"
)

st.plotly_chart(fig_region, use_container_width=True)

# ------------------------------------------------------------
# CORRELATION HEATMAP
# ------------------------------------------------------------

st.markdown("---")
st.subheader("🔥 Correlation Heatmap")

corr = filtered_df[
    [
        "Quantity",
        "Price",
        "CostPrice",
        "TotalSales",
        "FinalAmount",
        "Profit"
    ]
].corr()

fig_heatmap = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    aspect="auto",
    title="Correlation Matrix"
)

st.plotly_chart(fig_heatmap, use_container_width=True)
# ------------------------------------------------------------
# MACHINE LEARNING SALES PREDICTION
# ------------------------------------------------------------

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
        min_value=0.00,
        max_value=0.30,
        value=0.10,
        step=0.01
    )

if st.button("Predict Final Sales"):

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

# ------------------------------------------------------------
# DATASET EXPLORER
# ------------------------------------------------------------

st.markdown("---")
st.header("📋 Dataset Explorer")

rows = st.slider(
    "Select Number of Rows",
    5,
    100,
    10
)

st.dataframe(
    filtered_df.head(rows),
    use_container_width=True
)

# ------------------------------------------------------------
# DOWNLOAD DATASET
# ------------------------------------------------------------

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered Dataset",
    data=csv,
    file_name="filtered_dataset.csv",
    mime="text/csv"
)

# ------------------------------------------------------------
# SUMMARY STATISTICS
# ------------------------------------------------------------

st.markdown("---")
st.header("📈 Statistical Summary")

st.dataframe(
    filtered_df.describe(),
    use_container_width=True
)

# ------------------------------------------------------------
# BUSINESS INSIGHTS
# ------------------------------------------------------------

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

highest_payment = (
    filtered_df.groupby("PaymentMethod")["FinalAmount"]
    .sum()
    .idxmax()
)

best_customer = (
    filtered_df.groupby("CustomerName")["FinalAmount"]
    .sum()
    .idxmax()
)

st.info(f"""
✔ Highest Revenue Category : **{highest_category}**

✔ Highest Revenue Country : **{highest_country}**

✔ Best Payment Method : **{highest_payment}**

✔ Highest Revenue Customer : **{best_customer}**

✔ Total Revenue : **${total_revenue:,.2f}**

✔ Total Profit : **${total_profit:,.2f}**
""")

# ------------------------------------------------------------
# DATA INFORMATION
# ------------------------------------------------------------

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

# ------------------------------------------------------------
# RECORD COUNT
# ------------------------------------------------------------

st.metric(
    "Filtered Records",
    len(filtered_df)
)
# ------------------------------------------------------------
# ABOUT THE PROJECT
# ------------------------------------------------------------

st.markdown("---")
st.header("📖 About This Project")

st.write("""
The **E-Commerce Sales Analysis and Business Intelligence Dashboard**
is an end-to-end analytics solution developed using Python, Streamlit,
Pandas, Plotly, Scikit-learn, and Business Intelligence concepts.

The project demonstrates the complete data analytics lifecycle,
including data generation, cleaning, visualization,
feature engineering, statistical analysis,
machine learning, and dashboard development.
""")

# ------------------------------------------------------------
# PROJECT OBJECTIVES
# ------------------------------------------------------------

st.subheader("🎯 Project Objectives")

st.markdown("""
- Customer Behavior Analysis
- Product Performance Analysis
- Sales Trend Analysis
- Profitability Analysis
- Regional Performance Analysis
- Payment Method Analysis
- SQL-Style Business Reporting
- Sales Prediction using Machine Learning
""")

# ------------------------------------------------------------
# TOOLS & TECHNOLOGIES
# ------------------------------------------------------------

st.subheader("🛠 Tools & Technologies")

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

# ------------------------------------------------------------
# FINAL KPI SUMMARY
# ------------------------------------------------------------

st.markdown("---")
st.header("📊 Overall KPI Summary")

k1, k2, k3 = st.columns(3)

with k1:
    st.success(f"💰 Revenue\n\n${total_revenue:,.2f}")

with k2:
    st.success(f"📈 Profit\n\n${total_profit:,.2f}")

with k3:
    st.success(f"🛒 Orders\n\n{total_orders}")

k4, k5 = st.columns(2)

with k4:
    st.success(f"👥 Customers\n\n{total_customers}")

with k5:
    st.success(f"📦 Products\n\n{total_products}")

# ------------------------------------------------------------
# PROJECT CONCLUSION
# ------------------------------------------------------------

st.markdown("---")
st.header("📝 Project Conclusion")

st.success("""
This project successfully demonstrates a complete Business
Intelligence workflow for an E-Commerce business.

The dashboard enables users to:

✔ Monitor Revenue

✔ Track Profit

✔ Analyze Customers

✔ Evaluate Product Performance

✔ Study Sales Trends

✔ Compare Payment Methods

✔ Perform Statistical Analysis

✔ Predict Future Sales using Machine Learning

The dashboard supports data-driven decision making through
interactive visualizations and predictive analytics.
""")

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown("---")

st.markdown(
"""
<div style='text-align:center'>

### 🛒 E-Commerce Sales Analysis & Business Intelligence Dashboard

Built using

**Streamlit | Plotly | Pandas | Scikit-learn | Power BI**

---

© 2026 Mini Project

</div>
""",
unsafe_allow_html=True
)
