USE healthcare_analytics;

-- 1. Overall commercial KPIs
SELECT ROUND(SUM(revenue),2) AS total_revenue,
       ROUND(SUM(gross_profit),2) AS total_gross_profit,
       ROUND(SUM(gross_profit)/SUM(revenue)*100,2) AS gross_margin_pct,
       SUM(prescriptions) AS prescriptions,
       SUM(new_patients) AS new_patients_reached
FROM commercial_sales;

-- 2. Revenue and patient reach by region
SELECT region, ROUND(SUM(revenue),2) AS revenue,
       SUM(prescriptions) AS prescriptions,
       SUM(new_patients) AS new_patients,
       ROUND(SUM(gross_profit)/SUM(revenue)*100,2) AS margin_pct
FROM commercial_sales
GROUP BY region
ORDER BY revenue DESC;

-- 3. Product performance
SELECT product_name, ROUND(SUM(revenue),2) AS revenue,
       ROUND(SUM(gross_profit),2) AS gross_profit,
       SUM(prescriptions) AS prescriptions,
       SUM(new_patients) AS new_patients,
       ROUND(AVG(discount_pct)*100,2) AS avg_discount_pct
FROM commercial_sales
GROUP BY product_name
ORDER BY revenue DESC;

-- 4. High-potential doctors with low engagement
SELECT d.doctor_id, d.specialty, d.region, d.potential_segment,
       SUM(s.sales_calls) AS sales_calls,
       SUM(s.prescriptions) AS prescriptions,
       ROUND(SUM(s.revenue),2) AS revenue
FROM doctors d
JOIN commercial_sales s ON d.doctor_id=s.doctor_id
WHERE d.potential_segment='High'
GROUP BY d.doctor_id, d.specialty, d.region, d.potential_segment
HAVING SUM(s.sales_calls) < 85
ORDER BY revenue ASC
LIMIT 25;

-- 5. Sales-call effectiveness by segment
SELECT potential_segment,
       SUM(sales_calls) AS calls,
       SUM(prescriptions) AS prescriptions,
       ROUND(SUM(prescriptions)/NULLIF(SUM(sales_calls),0),2) AS prescriptions_per_call,
       ROUND(SUM(revenue)/NULLIF(SUM(sales_calls),0),2) AS revenue_per_call
FROM commercial_sales
GROUP BY potential_segment
ORDER BY revenue_per_call DESC;

-- 6. Monthly trend with MoM growth using LAG
WITH monthly AS (
    SELECT month, SUM(revenue) AS revenue
    FROM commercial_sales
    GROUP BY month
), x AS (
    SELECT month, revenue, LAG(revenue) OVER (ORDER BY month) AS prev_revenue
    FROM monthly
)
SELECT month, ROUND(revenue,2) AS revenue,
       ROUND((revenue-prev_revenue)/NULLIF(prev_revenue,0)*100,2) AS mom_growth_pct
FROM x
ORDER BY month;

-- 7. Top sales reps by revenue and patient reach
SELECT s.rep_id, r.rep_name, r.region,
       ROUND(SUM(s.revenue),2) AS revenue,
       SUM(s.new_patients) AS new_patients,
       SUM(s.sales_calls) AS sales_calls,
       ROUND(SUM(s.revenue)/NULLIF(SUM(s.sales_calls),0),2) AS revenue_per_call
FROM commercial_sales s
JOIN sales_reps r ON s.rep_id=r.rep_id
GROUP BY s.rep_id, r.rep_name, r.region
ORDER BY revenue DESC;

-- 8. Patient therapy status by product
SELECT product_name, therapy_status,
       COUNT(*) AS patients,
       ROUND(AVG(adherence_rate)*100,2) AS avg_adherence_pct
FROM patient_reach
GROUP BY product_name, therapy_status
ORDER BY product_name, patients DESC;

-- 9. Discontinuation rate by region
SELECT region, COUNT(*) AS patients,
       SUM(therapy_status='Discontinued') AS discontinued_patients,
       ROUND(SUM(therapy_status='Discontinued')/COUNT(*)*100,2) AS discontinuation_rate_pct
FROM patient_reach
GROUP BY region
ORDER BY discontinuation_rate_pct DESC;

-- 10. Rank products within each region
WITH region_product AS (
    SELECT region, product_name, SUM(revenue) AS revenue
    FROM commercial_sales
    GROUP BY region, product_name
)
SELECT region, product_name, ROUND(revenue,2) AS revenue,
       DENSE_RANK() OVER (PARTITION BY region ORDER BY revenue DESC) AS product_rank
FROM region_product
ORDER BY region, product_rank;
