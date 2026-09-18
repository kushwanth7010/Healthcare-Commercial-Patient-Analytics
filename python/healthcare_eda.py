import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sales = pd.read_csv(ROOT / "data/raw/commercial_sales.csv", parse_dates=["month"])
patients = pd.read_csv(ROOT / "data/raw/patient_reach.csv", parse_dates=["therapy_start_date"])

print("Rows:", len(sales))
print("Missing values:\n", sales.isna().sum().sort_values(ascending=False).head())

total_revenue = sales["revenue"].sum()
gross_profit = sales["gross_profit"].sum()
margin = gross_profit / total_revenue
prescriptions = sales["prescriptions"].sum()
new_patients = sales["new_patients"].sum()

print(f"Total Revenue: {total_revenue:,.0f}")
print(f"Gross Profit: {gross_profit:,.0f}")
print(f"Gross Margin: {margin:.2%}")
print(f"Prescriptions: {prescriptions:,}")
print(f"New Patients Reached: {new_patients:,}")

region = sales.groupby("region").agg(revenue=("revenue","sum"), gross_profit=("gross_profit","sum"), prescriptions=("prescriptions","sum"), new_patients=("new_patients","sum"), sales_calls=("sales_calls","sum")).sort_values("revenue", ascending=False)
region["revenue_per_call"] = region["revenue"] / region["sales_calls"]
print("\nRegional performance:\n", region)

product = sales.groupby("product_name").agg(revenue=("revenue","sum"), gross_profit=("gross_profit","sum"), prescriptions=("prescriptions","sum"), new_patients=("new_patients","sum")).sort_values("revenue", ascending=False)
product["margin_pct"] = product["gross_profit"] / product["revenue"]
print("\nProduct performance:\n", product)

doctor = sales.groupby(["doctor_id","potential_segment","region"]).agg(revenue=("revenue","sum"), calls=("sales_calls","sum"), prescriptions=("prescriptions","sum")).reset_index()
doctor["revenue_per_call"] = doctor["revenue"] / doctor["calls"].replace(0, np.nan)
opportunity = doctor[doctor["potential_segment"] == "High"].sort_values(["calls","revenue"], ascending=[True, True]).head(30)
(ROOT / "data/processed").mkdir(parents=True, exist_ok=True)
opportunity.to_csv(ROOT / "data/processed/high_potential_doctor_opportunities.csv", index=False)

status = patients["therapy_status"].value_counts()
discontinuation_rate = patients["therapy_status"].eq("Discontinued").mean()
print("\nTherapy status:\n", status)
print(f"Discontinuation Rate: {discontinuation_rate:.2%}")

monthly = sales.groupby("month")["revenue"].sum()
plt.figure(figsize=(10,5))
monthly.plot()
plt.title("Monthly Revenue Trend")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(ROOT / "data/processed/monthly_revenue.png", dpi=150)
plt.close()

region["revenue"].sort_values().plot(kind="barh", figsize=(8,5))
plt.title("Revenue by Region")
plt.tight_layout()
plt.savefig(ROOT / "data/processed/revenue_by_region.png", dpi=150)
plt.close()

print("\nSaved processed outputs successfully.")
