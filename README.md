🛍️ ETL and Analysis on Online Retail Data (PySpark)

End-to-end ETL and analytics pipeline built using PySpark to analyze large-scale e-commerce transaction data and derive business insights.

Overview

This project demonstrates a complete Extract–Transform–Load (ETL) workflow and analytical pipeline on an online retail dataset using PySpark, with supporting visualizations in Matplotlib.

The focus is on scalable data processing, feature engineering, and structured analysis to understand customer behavior, sales trends, and product performance.

Problem Context

E-commerce transaction data is typically:

Large in volume

Noisy and inconsistent

Difficult to analyze without distributed processing

This project uses Spark-based ETL to clean, transform, and analyze retail data efficiently while maintaining analytical reliability.

Dataset

Online Retail Dataset
Source: UCI Machine Learning Repository

UK-based online retail transactions

Time period: December 2010 – December 2011

Contains invoices, products, quantities, prices, and customer identifiers

Pipeline Flow

Extract
→ Clean
→ Transform
→ Feature Engineering
→ Analyze
→ Visualize

Each stage is designed to be reproducible and scalable.

What This Project Does
Data Loading

Loaded CSV data using spark.read.csv()

Applied schema inference for structured processing

Data Cleaning

Removed rows with missing values

Casted data types for quantity, price, and invoice date

Created transaction-level TotalValue feature

Feature Engineering

Extracted Year, Month, and Day of Week from invoice dates

Computed PurchaseCount per customer

Segmented customers into B2B and B2C based on purchasing frequency

Data Analysis

Identified top 10 best-selling products

Analyzed monthly and weekly sales trends

Calculated average order value per customer

Compared sales distribution across customer segments

Visualization

Bar charts for top-selling products

Line plots for monthly sales trends

Pie chart for B2B vs B2C customer distribution

Bar chart for weekly sales patterns

Key Insights

B2B customers contribute more frequently to transactions

A small set of products dominates overall sales volume

Sales peak during November and December, indicating seasonality

Most transactions occur mid-week (Tuesday–Thursday)

Tech Stack

Apache Spark (PySpark)

Python

Pandas

Matplotlib

Jupyter Notebook / Google Colab / Databricks

Project Structure
ETL-and-Analysis-on-Online-Retail-Data/
│
├── notebooks/        # PySpark analysis notebooks
├── data/             # Dataset files
├── outputs/          # Generated plots and results
├── README.md         # Project documentation
└── requirements.txt  # Dependencies

Why This Matters

This project demonstrates the ability to:

Handle large-scale structured data

Build Spark-based ETL workflows

Perform business-focused analytics on real-world data

These skills are essential for data engineering, analytics, and ML-adjacent roles.

Author

Diksha Singh
Data Scientist | ML Reliability & Data Quality Engineering
LinkedIn: https://www.linkedin.com/in/diksha-singh30

GitHub: https://github.com/Diksha2605
