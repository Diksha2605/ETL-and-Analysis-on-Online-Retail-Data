
🛍️ ETL and Analysis on Online Retail Data

This project demonstrates a comprehensive ETL (Extract, Transform, Load) pipeline and exploratory data analysis (EDA) using PySpark, Pandas, and Matplotlib on an e-commerce dataset. It includes customer segmentation, product analysis, sales trends, and key visualizations to extract meaningful business insights.
🚀 Project Overview

The goal of this project is to:

    Perform data cleaning and transformation using PySpark

    Engineer useful features like purchase frequency and total order value

    Identify customer segments (B2B and B2C)

    Analyze top-se

    lling products and sales trends

    Visualize findings using Python-based tools

📁 Dataset

    Dataset: Online Retail.csv

    Source: UCI Machine Learning Repository

    Description: Historical transactional data from a UK-based online retail store between 2010 and 2011.

🧰 Tech Stack
Tool/Library	Purpose
PySpark	Distributed processing & ETL
Pandas	Data manipulation
Matplotlib	Data visualization
Databricks Community Edition	Execution environment
📊 Key Analyses Performed
✅ ETL Process

    Null value handling and type casting

    Total order value calculation

    Date formatting for time-series analysis

✅ Feature Engineering

    Customer purchase frequency

    B2B vs B2C customer segmentation

    Year and Month extraction from timestamps

✅ Visual Insights

    📈 Top 10 Best-Selling Products

    📆 Monthly Sales Trends

    🧍 Customer Type Distribution (B2B vs B2C)

    📅 Sales by Day of the Week

    💰 Average Order Value by Customer

📸 Sample Visualizations
<img src="https://github.com/your-username/your-repo-name/blob/main/images/top_products.png" width="500"/> <p align="center">Top 10 Best-Selling Products</p> <img src="https://github.com/your-username/your-repo-name/blob/main/images/monthly_sales.png" width="500"/> <p align="center">Monthly Sales Trend</p>

    Note: Add generated plots to a folder named images/ and update the image links above.

📦 Setup Instructions

    Clone the repo:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Install required Python libraries:

pip install pyspark pandas matplotlib

Run the script:

    python etl_and_analysis_on_online_retail_data.py

    ⚠️ Ensure you have Java and Spark installed and properly configured.

💡 Future Enhancements

    Build predictive models for customer churn or product demand

    Automate ETL via Airflow or Apache NiFi

    Integrate with cloud-based storage (S3, GCS)

🙌 Acknowledgments

    Dataset: UCI Machine Learning Repository

    Author: Diksha
