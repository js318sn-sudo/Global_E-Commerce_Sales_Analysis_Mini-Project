# E-Commerce Sales Analysis & Business Intelligence Dashboard

## Project Overview

The **E-Commerce Sales Analysis & Business Intelligence Dashboard** is a complete end-to-end Data Analytics and Machine Learning project developed using **Python, Streamlit, Pandas, NumPy, Plotly, Scikit-learn, and Power BI**.

This project demonstrates the complete analytics lifecycle, including data generation, data preprocessing, exploratory data analysis (EDA), feature engineering, statistical analysis, interactive visualization, machine learning, dashboard development, and web application deployment.

The interactive Streamlit application enables users to analyze customer behavior, product performance, regional sales, profitability, payment trends, and sales forecasting through an intuitive Business Intelligence dashboard.

---

## Problem Statement

Modern e-commerce businesses generate massive volumes of customer, product, order, and payment data every day. Analyzing this information is essential for identifying business trends, understanding customer purchasing behavior, improving profitability, optimizing product performance, and supporting strategic business decisions.

This project performs comprehensive analysis using Python, SQL-style analytical operations with Pandas, statistical analysis, machine learning, and business intelligence visualization to provide meaningful insights for data-driven decision-making.

---

## Project Objectives

* Customer Behavior Analysis
* Product Performance Analysis
* Sales Trend Analysis
* Profitability Analysis
* Regional Performance Analysis
* Payment Method Analysis
* SQL-Style Business Reporting
* Interactive Business Intelligence Dashboard
* Sales Prediction using Machine Learning

---

## Live Streamlit Application

### Streamlit Deployment

https://globale-commercesalesanalysismini-project-tdfhfdcjnh5zyoncykzr.streamlit.app/

Explore the application to:

* View Business KPIs
* Analyze Customer Performance
* Analyze Product Performance
* Analyze Regional Sales
* Analyze Payment Methods
* Explore Sales Trends
* Predict Final Sales Amount using Machine Learning
* Download Filtered Dataset

---

## Business Intelligence Dashboard

![Business Intelligence Dashboard](Business_Intelligence_Dashboard.png) 

---

## Dataset Description

A custom synthetic E-Commerce Sales dataset was created to simulate real-world online business operations.

The project contains five datasets:

* customers.csv
* products.csv
* orders.csv
* payments.csv
* final_merged_dataset.csv

The final merged dataset combines customer information, product details, sales transactions, payment information, discounts, revenue, and profitability for complete business analysis.

---

## Project Workflow

1. Data Generation
2. Data Cleaning
3. Data Merging
4. Feature Engineering
5. Exploratory Data Analysis (EDA)
6. Statistical Analysis
7. Data Visualization
8. Machine Learning
9. Streamlit Dashboard Development
10. Business Intelligence Dashboard
11. Streamlit Deployment

---

## Feature Engineering

The following business features were created:

* TotalSales
* DiscountAmount
* FinalAmount
* Profit
* Profit Margin

---

## Exploratory Data Analysis

The project includes:

* Sales Trend Analysis
* Category-wise Revenue Analysis
* Product Performance Analysis
* Customer Behavior Analysis
* Regional Performance Analysis
* Payment Method Analysis
* Profit Analysis
* Correlation Analysis

---

## Machine Learning

### Model

* Linear Regression

### Input Features

* Quantity
* Price
* CostPrice
* Discount

### Target Variable

* FinalAmount

### Evaluation Metrics

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

### Model Performance

* R² Score: **0.86**

The model demonstrates good predictive performance for estimating the Final Sales Amount.

---

## Dashboard Features

* Interactive KPI Dashboard
* Revenue Analysis
* Profit Analysis
* Customer Insights
* Product Performance
* Regional Sales Analysis
* Payment Analysis
* Correlation Heatmap
* Machine Learning Prediction
* Dataset Explorer
* Download Filtered Dataset

---

## Tools & Technologies

* Python
* Pandas
* NumPy
* Plotly
* Streamlit
* Scikit-learn
* Power BI
* Jupyter Notebook
* Git
* GitHub

---

## Project Structure

```text
E-Commerce-Sales-Analysis/
│
├── app.py
├── requirements.txt
├── README.md
├── Mini-Project.ipynb
├── customers.csv
├── products.csv
├── orders.csv
├── payments.csv
├── final_merged_dataset.csv
└── Business_Intelligence_Dashboard.png
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/E-Commerce-Sales-Analysis.git
```

Move into the project directory:

```bash
cd E-Commerce-Sales-Analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Streamlit Deployment

**Live Application**

https://globale-commercesalesanalysismini-project-tdfhfdcjnh5zyoncykzr.streamlit.app/

---

## Key Business Insights

* Beauty generated the highest revenue among all product categories.
* Asia generated the highest overall revenue, followed by Europe and North America.
* UPI contributed the highest revenue among payment methods.
* Strong positive correlation exists between Price, Total Sales, and Final Amount.
* A small group of customers contributed a significant share of total revenue.
* Monthly sales remained consistent throughout 2023 and 2024.
* The Linear Regression model achieved an R² Score of approximately **0.86**.

---

## Final KPIs

| KPI             |      Value |
| --------------- | ---------: |
| Total Revenue   | **10.41M** |
| Total Profit    |  **1.28M** |
| Total Orders    |  **5,000** |
| Total Customers |    **500** |
| Total Products  |    **200** |

---

## Future Enhancements

* Real-time Database Integration
* Cloud Deployment
* User Authentication
* Customer Recommendation System
* Advanced Machine Learning Models
* AI-Based Sales Forecasting
* Interactive Business Reports

---

## Conclusion

This project demonstrates a complete Business Intelligence and Data Analytics solution for E-Commerce Sales Analysis using **Python, Streamlit, Plotly, Scikit-learn, and Power BI**.

The project integrates data preprocessing, exploratory data analysis, feature engineering, interactive visualization, predictive analytics, and dashboard development into a single web application. It provides meaningful business insights and supports data-driven decision-making while showcasing practical implementation of modern data analytics and business intelligence techniques.

