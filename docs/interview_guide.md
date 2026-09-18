# Interview Explanation

## 30-second version
"I built a Healthcare Commercial & Patient Reach Analytics project to simulate how a life-sciences analytics team could evaluate sales effectiveness and patient reach. I used Python for cleaning and exploratory analysis, SQL for business queries and segmentation, and Power BI for executive dashboards. The main questions were which regions and products drive performance, whether sales-call activity translates into prescriptions, which high-potential doctors are under-engaged, and where patient discontinuation is elevated."

## 90-second version
"The project uses a synthetic healthcare commercial dataset with doctor, product, sales-representative, prescription, revenue, patient-reach and adherence information. I designed it as a star-schema style model. In SQL I calculated regional and product KPIs, month-over-month trends using LAG, sales-call effectiveness, high-potential doctor opportunities, and product rankings using window functions. In Python I performed data-quality checks, EDA, regional and product aggregation, and opportunity segmentation. In Power BI I created pages for executive KPIs, regional performance, products, doctor segmentation, sales-force effectiveness and patient reach. The goal was not just visualization; it was to turn the analysis into commercial actions such as targeting under-engaged high-potential doctors, reviewing discount-heavy products with weak margins, and investigating regions with high patient discontinuation."

## Questions you should be ready for

### Why did you choose this project?
Because it combines my life-sciences background with business analytics and lets me solve commercial healthcare problems using SQL, Python and Power BI.

### Why SQL and Python both?
SQL is efficient for extracting, joining, grouping and ranking structured business data. Python is better for flexible cleaning, exploratory analysis, automation and statistical work.

### Why Power BI?
It lets stakeholders explore KPIs interactively and drill from executive-level performance into regions, products, doctors and patient segments.

### What is the most important KPI?
There is no single KPI. Revenue must be considered with margin, prescriptions, patient reach, sales-call efficiency and discontinuation. A product can grow revenue while destroying margin through excessive discounting.

### What is patient reach?
In this project, patient reach is the number of synthetic patients newly associated with therapy/product use during the analysis period. It is a commercial analytics proxy, not a clinical outcome.

### How did you identify doctor opportunities?
I segmented doctors by potential and compared engagement (sales calls) with prescriptions and revenue. High-potential doctors with relatively low engagement are candidates for commercial prioritization.

### What SQL concepts did you use?
Joins, GROUP BY, HAVING, CTEs, CASE logic, aggregate functions, LAG, DENSE_RANK and partitioned window functions.

### What would you improve with real data?
I would add claims-based patient journeys, payer/channel variables, marketing-campaign exposure, territory targets, product launch dates, richer physician segmentation and statistically controlled attribution.

## Important honesty point
The repository uses synthetic/de-identified data. Never claim it is real patient-level data.
