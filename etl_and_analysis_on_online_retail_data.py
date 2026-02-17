# ETL and Analysis on Online Retail Data

End-to-end ETL and analytical pipeline built using PySpark for large-scale e-commerce transaction data.

## Overview
This repository contains a Spark-based ETL workflow and analytical pipeline designed to process, clean, and analyze online retail transaction data. The project focuses on scalable data processing, structured transformations, and reproducible analysis to derive reliable business insights from raw transactional data.

## Dataset
Source: UCI Machine Learning Repository  
Domain: Online retail transactions  
Time period: December 2010 – December 2011  

The dataset includes invoice-level records with product, quantity, pricing, and customer identifiers.

## Pipeline
Extract  
Transform  
Validate  
Analyze  

Each stage is implemented using PySpark to support distributed processing and scalability.

## Processing Steps

### Data Ingestion
Raw CSV data is loaded using Spark’s DataFrame API with schema inference enabled to ensure structured access to fields.

### Data Cleaning
Invalid and incomplete records are removed. Data types for numerical and temporal fields are explicitly cast, and transaction-level total value is computed to support downstream analysis.

### Feature Engineering
Temporal features (year, month, day of week) are derived from invoice timestamps. Customer-level purchase frequency is computed and used to segment customers into business and consumer groups.

### Analysis
The pipeline computes product-level sales volume, customer-level order statistics, and temporal sales trends. Aggregations are performed to support both exploratory analysis and business interpretation.

### Visualization
Aggregated results are visualized using Matplotlib to highlight sales trends, customer distribution, and product performance.

## Outputs
Cleaned and validated transaction dataset  
Aggregated sales metrics  
Customer segmentation results  
Temporal trend visualizations  

## Technology Stack
Python  
Apache Spark (PySpark)  
Pandas  
Matplotlib  

## Repository Structure
ETL-and-Analysis-on-Online-Retail-Data/
├── notebooks/
├── data/
├── outputs/
├── README.md
└── requirements.txt

## Purpose
The project demonstrates the use of distributed data processing to build reliable ETL pipelines and perform structured analytics on real-world retail data. It emphasizes data quality, scalability, and reproducibility rather than ad-hoc analysis.

## Author
Diksha Singh  
Data Scientist – ML Reliability & Data Quality  
LinkedIn: https://www.linkedin.com/in/diksha-singh30  
GitHub: https://github.com/Diksha2605
