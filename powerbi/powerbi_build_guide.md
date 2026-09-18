# Power BI Build Guide

## Data Model
Create a Date table and relate:
- Date[Date] -> commercial_sales[month]
- doctors[doctor_id] -> commercial_sales[doctor_id]
- products[product_id] -> commercial_sales[product_id]
- sales_reps[rep_id] -> commercial_sales[rep_id]
- doctors[doctor_id] -> patient_reach[doctor_id]

Use single-direction filters from dimensions to facts.

## Core DAX Measures

```DAX
Total Revenue = SUM(commercial_sales[revenue])

Gross Profit = SUM(commercial_sales[gross_profit])

Gross Margin % = DIVIDE([Gross Profit], [Total Revenue])

Total Prescriptions = SUM(commercial_sales[prescriptions])

New Patients Reached = SUM(commercial_sales[new_patients])

Repeat Patients = SUM(commercial_sales[repeat_patients])

Total Sales Calls = SUM(commercial_sales[sales_calls])

Revenue per Call = DIVIDE([Total Revenue], [Total Sales Calls])

Prescriptions per Call = DIVIDE([Total Prescriptions], [Total Sales Calls])

Avg Discount % = AVERAGE(commercial_sales[discount_pct])

Active Patients =
CALCULATE(COUNTROWS(patient_reach), patient_reach[therapy_status] = "Active")

Discontinued Patients =
CALCULATE(COUNTROWS(patient_reach), patient_reach[therapy_status] = "Discontinued")

Discontinuation Rate % =
DIVIDE([Discontinued Patients], COUNTROWS(patient_reach))

Avg Adherence % = AVERAGE(patient_reach[adherence_rate])

Revenue LY =
CALCULATE([Total Revenue], SAMEPERIODLASTYEAR('Date'[Date]))

YoY Revenue Growth % =
DIVIDE([Total Revenue] - [Revenue LY], [Revenue LY])
```

## Page 1 — Executive Overview
Cards:
- Total Revenue
- Gross Profit
- Gross Margin %
- Total Prescriptions
- New Patients Reached
- Discontinuation Rate %

Visuals:
- Monthly Revenue Trend
- Revenue by Region
- Revenue by Product
- New Patients by Region
- Product / Region slicers

## Page 2 — Regional Performance
- Revenue by State
- Region x Product matrix with Revenue, Margin, Prescriptions
- Revenue per Call by Region
- New Patient Reach by Region
- MoM / YoY trends

## Page 3 — Product & Therapy Analytics
- Revenue / Gross Profit by Product
- Prescriptions by Product
- Margin % by Product
- Avg Discount % vs Margin %
- New vs Repeat Patients

## Page 4 — Doctor Segmentation
- High / Medium / Low potential segment KPIs
- Scatter: Sales Calls vs Revenue, size = prescriptions
- High-potential / low-engagement doctor table
- Specialty performance

## Page 5 — Sales Force Effectiveness
- Revenue by Sales Rep
- Revenue per Call
- Prescriptions per Call
- Patient reach by Rep
- Rank reps by region

## Page 6 — Patient Reach & Adherence
- Active / Completed / Discontinued patients
- Discontinuation rate by product
- Adherence by condition
- Patient reach by age band / channel / region
- Therapy starts over time

## Page 7 — Recommendations
Create 4-6 evidence-backed recommendation cards only after validating the dashboard findings.
