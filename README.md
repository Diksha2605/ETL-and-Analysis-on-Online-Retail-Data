# 🛍️ ETL and Analysis on Online Retail Data using PySpark

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline and data analysis on an **e-commerce retail dataset** using **PySpark**, with additional visualizations in **Matplotlib**. It aims to identify customer behavior, top products, sales trends, and customer segmentation to derive actionable business insights.

---

## 🚀 Project Overview

The main objectives of this project are:

- ✅ Perform data extraction, cleaning, and transformation on retail data using PySpark.
- 📊 Analyze customer behavior, sales trends, and best-selling products.
- 🧠 Segment customers into B2B and B2C based on their purchasing frequency.
- 📈 Visualize sales patterns monthly and weekly to identify peak periods.

---

## 📂 Dataset Used

- **Name:** Online Retail Dataset
- **Source:** UCI Machine Learning Repository
- **Description:** Transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.

---

## 🧰 Technologies & Tools

- Apache Spark (PySpark)
- Python (Pandas, Matplotlib)
- Google Colab / Databricks
- Jupyter Notebook environment

---

## 🔧 Steps Performed

### 1. **Data Loading and Schema Inference**
- Loaded CSV using `spark.read.csv()` with schema inference.

### 2. **Data Cleaning**
- Dropped rows with missing values.
- Cast data types (`Quantity`, `UnitPrice`, `InvoiceDate`).
- Created `TotalValue` for each transaction.

### 3. **Feature Engineering**
- Extracted `Year`, `Month`, and `DayOfWeek` from `InvoiceDate`.
- Calculated `PurchaseCount` per customer.
- Added customer segmentation: `B2B` vs `B2C`.

### 4. **Data Analysis**
- Top 10 best-selling products
- Monthly and weekly sales trends
- Average order value per customer
- Sales distribution by customer type

### 5. **Visualization**
- Horizontal bar charts for top products
- Line plot for monthly sales
- Pie chart for B2B vs B2C distribution
- Bar chart for weekly sales

---

## 📊 Sample Outputs

| Analysis Type | Output Example |
|---------------|----------------|
| Top Products | ![Top Products](#) |
| Monthly Sales Trend | ![Monthly Sales](#) |
| Customer Type Distribution | ![Customer Pie](#) |
| Weekly Sales | ![Weekly Sales](#) |

---

## 📈 Key Insights

- 📌 **B2B customers** contribute more frequently to transactions.
- 🥇 Certain products dominate the sales volume (e.g., gift items).
- 🗓️ **November and December** see peak sales, indicating seasonal trends.
- 📅 Most sales happen mid-week (Tuesday to Thursday).

---

## 📁 Project Structure

