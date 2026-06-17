#  E-Commerce Sales Analysis and Business Intelligence Dashboard

## Project Overview  
This project is a complete end-to-end data analytics and machine learning solution for an e-commerce business. It includes data generation, data cleaning, exploratory data analysis, feature creation, visualization, business intelligence dashboard, and predictive modeling.

---

## Problem Statement  

The rapid growth of e-commerce businesses generates large volumes of sales, customer, product, and payment data. Analyzing this data is essential for understanding customer purchasing behavior, identifying top-performing products, tracking sales trends, evaluating profitability, and improving business decision-making.

This project aims to perform a comprehensive analysis of e-commerce sales data using Python, Pandas, SQL-style analytical operations, data visualization, statistical techniques, and machine learning. The focus is on extracting meaningful insights from business data, identifying sales patterns, evaluating customer and product performance, and supporting data-driven decision-making through analytical reporting and dashboard development.

---

## Objectives

- Customer Behavior Analysis  
- Product Performance Analysis  
- Sales Trend Analysis  
- Profitability Analysis  
- Regional Performance Analysis  
- Payment Analysis  
- SQL-Style Business Reporting and Analytical Operations  
- Sales Prediction using Machine Learning  

---

## Business Intelligence Dashboard

![Business Intelligence Dashboard](Business_Intelligence_Dashboard.png)

---

## Dataset Selection  

A custom E-Commerce Sales dataset was created to simulate real-world online business operations. The dataset consists of four interconnected tables: Customers, Products, Orders, and Payments.

These datasets contain customer details, product information, order transactions, sales amounts, discounts, profits, payment methods, and payment status.

The data was merged and analyzed using Pandas operations such as filtering, grouping, aggregation, joins, and sorting.

This dataset supports data cleaning, exploratory data analysis (EDA), feature engineering, statistical analysis, visualization, machine learning, and business intelligence reporting using Power BI.

---

## Datasets Used

- customers.csv – Customer information  
- products.csv – Product details and pricing  
- orders.csv – Order and sales transactions  
- payments.csv – Payment methods and status
- final_merged_dataset.csv -  Final merged dataset created by combining all four datasets using CustomerID, ProductID, and OrderID for complete analysis and modeling.

---

## Tools & Technologies

- Python  
- Pandas
- NumPy  
- Matplotlib
- Seaborn  
- Scikit-learn  
- Power BI (Business Intelligence Dashboard)
- Jupyter Notebook  

---

## Project Workflow

### 1. Data Generation
Synthetic datasets created for:
- Customers  
- Products  
- Orders  
- Payments  

---

### 2. Data Cleaning
- Handled missing values  
- Removed duplicates  
- Converted data types  

---

### 3. Data Merging
Merged datasets using:
- CustomerID  
- ProductID  
- OrderID  

---

### 4. Feature Creation
- TotalSales  
- DiscountAmount  
- FinalAmount  
- Profit  
- Profit Margin  

---

### 5. Exploratory Data Analysis
- Sales distribution  
- Category-wise analysis  
- Country-wise performance  
- Customer segmentation  

---

### 6. Machine Learning Model
- Linear Regression model  
- Predicts Final Sales Amount  
- Evaluated using MAE, MSE, R² Score  

---

### 7. Business Intelligence Dashboard
Created using Power BI:
- Revenue analysis  
- Profit analysis  
- Customer insights  
- Product performance  
- Time series trends  

---

## Key Insights

- Beauty is the highest revenue-generating category, followed by Sports and Accessories.
- Asia generated the highest revenue (4.01M), followed by Europe (2.25M) and North America (2.18M).
- UPI contributed the highest revenue among payment methods.
- Strong positive correlation exists between Price, Total Sales, and Final Amount.
- Profitability varies significantly across product categories, with some categories generating negative profit.
- Customer purchasing behavior shows that a small group of customers contributes a large share of total revenue.
- Monthly sales remained consistent across 2023 and 2024 with revenue exceeding 10.4 million overall.
- The Linear Regression model achieved an R² score of approximately 0.86, indicating good predictive performance.

---

## Machine Learning Performance
- Model: Linear Regression
- Evaluation Metrics:
- MAE
- MSE
- R² Score (~0.86)
- Good predictive performance for sales estimation.

---

## Final Deliverables
- Mini-Project.ipynb  
- Business_Intelligence_Dashboard.png
- README.md  
- customers.csv  
- products.csv  
- orders.csv  
- payments.csv
- final_merged_dataset.csv

___

##  Final KPIs  
- Total Revenue: ~10.4M  
- Total Profit: ~1.27M  
- Total Orders: 5000  
- Total Customers: 500  
- Total Products: 200
  
---

## Conclusion
This project demonstrates a complete data analytics pipeline including data preprocessing, visualization, machine learning, and business intelligence reporting for real-world e-commerce analysis using Power BI.
