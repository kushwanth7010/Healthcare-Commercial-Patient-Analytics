-- Healthcare Commercial & Patient Reach Analytics
-- SQL dialect: MySQL 8+

CREATE DATABASE IF NOT EXISTS healthcare_analytics;
USE healthcare_analytics;

CREATE TABLE products (
    product_name VARCHAR(100),
    therapy_area VARCHAR(100),
    unit_price DECIMAL(12,2),
    gross_margin_pct DECIMAL(8,4),
    product_id VARCHAR(10) PRIMARY KEY
);

CREATE TABLE doctors (
    doctor_id VARCHAR(10) PRIMARY KEY,
    doctor_name VARCHAR(100),
    specialty VARCHAR(100),
    region VARCHAR(50),
    state VARCHAR(100),
    potential_segment VARCHAR(20),
    avg_monthly_patient_volume INT
);

CREATE TABLE sales_reps (
    rep_id VARCHAR(10) PRIMARY KEY,
    rep_name VARCHAR(100),
    region VARCHAR(50),
    years_experience INT
);

CREATE TABLE commercial_sales (
    month DATE,
    doctor_id VARCHAR(10),
    rep_id VARCHAR(10),
    product_id VARCHAR(10),
    product_name VARCHAR(100),
    region VARCHAR(50),
    state VARCHAR(100),
    specialty VARCHAR(100),
    potential_segment VARCHAR(20),
    sales_calls INT,
    prescriptions INT,
    units_sold INT,
    discount_pct DECIMAL(8,4),
    revenue DECIMAL(14,2),
    cost DECIMAL(14,2),
    new_patients INT,
    repeat_patients INT,
    gross_profit DECIMAL(14,2),
    gross_margin_pct DECIMAL(8,4),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id),
    FOREIGN KEY (rep_id) REFERENCES sales_reps(rep_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE patient_reach (
    patient_id VARCHAR(15) PRIMARY KEY,
    age_band VARCHAR(20),
    `condition` VARCHAR(100),
    product_name VARCHAR(100),
    doctor_id VARCHAR(10),
    region VARCHAR(50),
    state VARCHAR(100),
    therapy_start_date DATE,
    therapy_status VARCHAR(30),
    adherence_rate DECIMAL(8,4),
    channel VARCHAR(50),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);
