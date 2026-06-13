# E-Commerce Sales Analysis and Business Intelligence Dashboard

## Project Overview
This project is a complete end-to-end data analytics and machine learning solution for an e-commerce business. It includes data generation, data cleaning, exploratory data analysis, feature creation, visualization, business intelligence dashboard, and predictive modeling.

---

## Problem Statement

The rapid growth of e-commerce businesses generates large volumes of sales, customer, product, and payment data. Analyzing this data is essential for understanding customer purchasing behavior, identifying top-performing products, tracking sales trends, evaluating profitability, and improving business decision-making. This project aims to perform a comprehensive analysis of e-commerce sales data using Python, Pandas, SQL-style analytical operations, data visualization, statistical techniques, and machine learning. The project focuses on extracting meaningful insights from business data, identifying sales patterns, evaluating customer and product performance, and supporting data-driven decision-making through analytical reporting and dashboard development.

### Objectives

- Customer Behavior Analysis
- Product Performance Analysis
- Sales Trend Analysis
- Profitability Analysis
- Regional Performance Analysis
- Payment Analysis
- SQL-Style Business Reporting and Analytical Operations
- Sales Prediction using Machine Learning

---

## Dataset Selection

For this project, a custom E-Commerce Sales dataset was created to simulate real-world online business operations. The dataset consists of four interconnected tables: Customers, Products, Orders, and Payments. These datasets contain information related to customer details, product information, order transactions, sales amounts, discounts, profits, payment methods, and payment status.

The data from multiple tables was integrated and analyzed using Pandas operations such as filtering, grouping, aggregation, joins, sorting, and business reporting. The combined dataset was used to study sales performance, customer behavior, product trends, revenue generation, profitability, and business growth patterns.

This dataset provides a strong foundation for data cleaning, exploratory data analysis (EDA), feature engineering, statistical analysis, data visualization, machine learning, and business intelligence reporting.

---

### Datasets Used

- customers.csv – Customer information
- products.csv – Product details and pricing information
- orders.csv – Order and sales transaction records
- payments.csv – Payment methods and payment status details
- final_merged_dataset.csv – Integrated dataset created by merging all datasets for analysis

These datasets were analyzed using Python, Pandas, statistical techniques, data visualization, machine learning, and business intelligence methods to generate meaningful insights and support data-driven decision-making.

---

## Tools & Technologies
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Power BI
- Jupyter Notebook

---

## Project Workflow

### 1. Data Generation
Synthetic datasets created for:
- Customers
- Products
- Orders
- Payments

### 2. Data Cleaning
- Handled missing values
- Removed duplicates
- Converted data types

### 3. Data Merging
All datasets merged into a single dataset using:
- CustomerID
- ProductID
- OrderID

### 4. Feature Creation
- TotalSales
- DiscountAmount
- FinalAmount
- Profit
- Profit Margin

### 5. Exploratory Data Analysis
- Sales distribution
- Category-wise analysis
- Country-wise performance
- Customer segmentation

### 6. Machine Learning Model
- Linear Regression model used
- Predicts Final Sales Amount
- Evaluated using MAE, MSE, R2 Score

### 7. Business Intelligence Dashboard
Created using Power BI:
- Revenue analysis
- Profit analysis
- Customer insights
- Product performance
- Time series trends

---

## Key Insights
- Electronics and Beauty are top performing categories
- USA and Japan generate highest revenue
- UPI is the most used payment method
- High correlation between price and sales
- Profit varies significantly across categories

---

## Machine Learning Performance
- Model: Linear Regression
- R2 Score: ~0.86
- Good predictive performance for sales estimation

---

## Final Deliverables
- Mini-Project.ipynb
- Dashboard.pbix
- README.md
- customers.csv
- products.csv
- orders.csv
- payments.csv
- final_merged_dataset.csv
  
---

## Conclusion
This project demonstrates a complete data analytics pipeline including data preprocessing, visualization, machine learning, and business intelligence reporting for real-world e-commerce analysis.
