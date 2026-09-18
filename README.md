# Healthcare Commercial & Patient Reach Analytics

## Project Summary
A portfolio-ready Business Analyst project that evaluates pharmaceutical commercial performance and patient reach using SQL, Python, and Power BI.

The dataset in this repository is **fully synthetic and de-identified**. It contains no real patient identities or protected health information.

## Business Questions
1. Which regions and products drive revenue and gross profit?
2. Where is patient reach strongest or weakest?
3. Which high-potential doctors are under-engaged?
4. How effective are sales calls in generating prescriptions and revenue?
5. Which products have high discontinuation or lower adherence?
6. Which sales representatives need support?
7. Where should the commercial team prioritize next-quarter effort?

## Dataset
- `commercial_sales.csv`: doctor-product-month commercial activity
- `doctors.csv`: specialty, geography, potential segment and patient volume
- `sales_reps.csv`: representative-to-region mapping
- `products.csv`: therapy area, price and expected margin
- `patient_reach.csv`: synthetic patient journey, therapy status and adherence

Generated rows:
- Commercial sales: 9,846
- Doctors: 350
- Sales reps: 25
- Synthetic patients: 18,000

## Tools
- SQL (MySQL 8+)
- Python: Pandas, NumPy, Matplotlib
- Power BI: Power Query, data modeling, DAX
- Git/GitHub

## Recommended Workflow
1. Run `python/generate_synthetic_data.py` to recreate the full raw dataset.
2. Run `python/healthcare_eda.py` for exploratory analysis and processed outputs.
3. Load the generated tables into MySQL.
4. Run the SQL analysis queries.
5. Import the tables into Power BI.
6. Build the dashboard pages described in `powerbi/powerbi_build_guide.md`.
7. Write evidence-backed business recommendations from the dashboard.

## Star Schema
- Fact: `commercial_sales`
- Dimensions: `doctors`, `products`, `sales_reps`, Date
- Patient fact: `patient_reach`

## Resume-safe project title
**Healthcare Commercial & Patient Reach Analytics | Python, SQL, Power BI**

> This is a synthetic commercial healthcare analytics case study, not real patient or company data.

## Repository Structure
```text
data/
  processed/
python/
sql/
powerbi/
docs/
README.md
```
