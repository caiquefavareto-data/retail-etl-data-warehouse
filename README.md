# Retail Data Warehouse & Automated ETL Pipeline

##  Business Problem
A supermarket chain was struggling with fragmented information. Raw data was scattered across transactional databases (ERP), legacy CSV files, and external APIs. Because the data was unorganized and not integrated, the business could not easily track inventory or analyze regional sales, leading to hidden operational costs.

##  The Solution (Action)
I designed and built an automated ETL pipeline using Python and SQL to resolve this fragmentation:
* **Extract:** Collected data from diverse heterogeneous sources.
* **Transform:** Cleaned null values, removed duplicates, and standardized formats to ensure data quality.
* **Load:** Loaded the clean data into a Data Warehouse using a **Star Schema** architecture. Created a central Fact table for sales metrics, surrounded by Dimension tables (Customers, Products, Stores, Date).

##  The Impact
By structuring the data this way, I enabled fast OLAP multidimensional analysis. The business can now instantly slice and dice the data to see which store generates the highest profit margin or how external factors affect specific product sales. This data foundation directly helps the company optimize inventory, forecast demand, and reduce costs.

##  Repository Structure
* `data/`: Raw and processed datasets.
* `sql/`: DDL for Star Schema and OLAP views.
* `src/`: Python scripts for Extract, Transform, and Load operations.
