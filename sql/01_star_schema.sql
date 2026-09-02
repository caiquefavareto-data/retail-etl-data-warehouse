-- DDL: Star Schema Architecture for Retail Data Warehouse

-- Dimension Tables
CREATE TABLE Dim_Store (
    store_key INT PRIMARY KEY,
    store_name VARCHAR(100),
    city VARCHAR(50),
    region VARCHAR(50)
);

CREATE TABLE Dim_Product (
    product_key INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price DECIMAL(10,2)
);

CREATE TABLE Dim_Date (
    date_key INT PRIMARY KEY,
    full_date DATE,
    day_of_week VARCHAR(15),
    month_name VARCHAR(15),
    year INT
);

-- Fact Table
CREATE TABLE Fact_Sales (
    sales_id INT PRIMARY KEY,
    date_key INT,
    store_key INT,
    product_key INT,
    quantity_sold INT,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (date_key) REFERENCES Dim_Date(date_key),
    FOREIGN KEY (store_key) REFERENCES Dim_Store(store_key),
    FOREIGN KEY (product_key) REFERENCES Dim_Product(product_key)
);
