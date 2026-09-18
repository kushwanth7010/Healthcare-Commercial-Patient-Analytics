from pathlib import Path
import random
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

rng = np.random.default_rng(42)
random.seed(42)

regions = ["North", "South", "East", "West", "Central"]
states = {
    "North": ["Delhi", "Punjab", "Haryana", "Uttar Pradesh"],
    "South": ["Telangana", "Karnataka", "Tamil Nadu", "Kerala"],
    "East": ["West Bengal", "Odisha", "Bihar", "Assam"],
    "West": ["Maharashtra", "Gujarat", "Rajasthan", "Goa"],
    "Central": ["Madhya Pradesh", "Chhattisgarh", "Jharkhand"],
}
specialties = ["Cardiology", "Diabetology", "General Medicine", "Pulmonology", "Neurology"]

products = pd.DataFrame([
    ["CardioPlus", "Cardiology", 1250, 0.36],
    ["GlucoCare", "Diabetology", 980, 0.32],
    ["RespiraX", "Pulmonology", 1420, 0.40],
    ["NeuroZen", "Neurology", 1650, 0.42],
    ["MediCore", "General Medicine", 720, 0.28],
], columns=["product_name", "therapy_area", "unit_price", "gross_margin_pct"])
products["product_id"] = [f"P{i:03d}" for i in range(1, len(products) + 1)]

n_doctors = 350
doctor_rows = []
for i in range(n_doctors):
    region = random.choice(regions)
    state = random.choice(states[region])
    specialty = random.choice(specialties)
    potential = random.choices(["High", "Medium", "Low"], weights=[0.28, 0.47, 0.25])[0]
    monthly_patients = int(max(40, rng.normal({"High": 420, "Medium": 260, "Low": 140}[potential], 55)))
    doctor_rows.append([f"D{i+1:04d}", f"Doctor_{i+1:04d}", specialty, region, state, potential, monthly_patients])
doctors = pd.DataFrame(doctor_rows, columns=["doctor_id", "doctor_name", "specialty", "region", "state", "potential_segment", "avg_monthly_patient_volume"])

n_reps = 25
rep_rows = []
for i in range(n_reps):
    region = regions[i % len(regions)]
    rep_rows.append([f"R{i+1:03d}", f"Rep_{i+1:03d}", region, int(rng.integers(1, 8))])
reps = pd.DataFrame(rep_rows, columns=["rep_id", "rep_name", "region", "years_experience"])

months = pd.date_range("2025-01-01", "2026-12-01", freq="MS")
rows = []
primary_product = {
    "Cardiology": "CardioPlus",
    "Diabetology": "GlucoCare",
    "Pulmonology": "RespiraX",
    "Neurology": "NeuroZen",
    "General Medicine": "MediCore",
}

for month in months:
    seasonal = 1 + 0.08 * np.sin((month.month - 1) / 12 * 2 * np.pi)
    for _, doctor in doctors.iterrows():
        primary = primary_product[doctor.specialty]
        selected_products = [primary]
        if rng.random() < 0.22:
            selected_products.append(random.choice(products.product_name.tolist()))
        for product_name in set(selected_products):
            product = products.loc[products.product_name == product_name].iloc[0]
            rep_pool = reps[reps.region == doctor.region]
            rep = rep_pool.sample(1, random_state=int(rng.integers(0, 1_000_000))).iloc[0]
            potential_multiplier = {"High": 1.55, "Medium": 1.0, "Low": 0.62}[doctor.potential_segment]
            specialty_match = 1.28 if product_name == primary else 0.58
            sales_calls = max(1, int(rng.poisson(4.5 * potential_multiplier)))
            prescriptions = max(0, int(rng.poisson(18 * potential_multiplier * specialty_match * seasonal + sales_calls * 1.9)))
            units_sold = max(prescriptions, int(prescriptions * rng.uniform(1.05, 1.35)))
            discount_pct = float(np.clip(rng.normal(0.08, 0.025), 0.02, 0.18))
            revenue = units_sold * product.unit_price * (1 - discount_pct)
            cost = revenue * (1 - product.gross_margin_pct) * rng.uniform(0.96, 1.04)
            new_patients = max(0, int(prescriptions * rng.uniform(0.22, 0.44)))
            repeat_patients = max(0, prescriptions - new_patients)
            rows.append([month.strftime("%Y-%m-%d"), doctor.doctor_id, rep.rep_id, product.product_id, product_name, doctor.region, doctor.state, doctor.specialty, doctor.potential_segment, sales_calls, prescriptions, units_sold, round(discount_pct, 4), round(revenue, 2), round(cost, 2), new_patients, repeat_patients])

sales = pd.DataFrame(rows, columns=["month", "doctor_id", "rep_id", "product_id", "product_name", "region", "state", "specialty", "potential_segment", "sales_calls", "prescriptions", "units_sold", "discount_pct", "revenue", "cost", "new_patients", "repeat_patients"])
sales["gross_profit"] = (sales["revenue"] - sales["cost"]).round(2)
sales["gross_margin_pct"] = (sales["gross_profit"] / sales["revenue"]).replace([np.inf, -np.inf], np.nan).fillna(0).round(4)

conditions = ["Hypertension", "Type 2 Diabetes", "Asthma", "Migraine", "General Chronic Care"]
condition_product = {"Hypertension": "CardioPlus", "Type 2 Diabetes": "GlucoCare", "Asthma": "RespiraX", "Migraine": "NeuroZen", "General Chronic Care": "MediCore"}
patient_rows = []
for i in range(18_000):
    condition = random.choice(conditions)
    product_name = condition_product[condition]
    doctor = doctors.sample(1, random_state=int(rng.integers(0, 1_000_000))).iloc[0]
    start_date = pd.Timestamp("2025-01-01") + pd.Timedelta(days=int(rng.integers(0, 690)))
    status = random.choices(["Active", "Completed", "Discontinued"], weights=[0.55, 0.23, 0.22])[0]
    adherence = float(np.clip(rng.normal({"Active": 0.84, "Completed": 0.78, "Discontinued": 0.48}[status], 0.12), 0.1, 1.0))
    age_band = random.choices(["18-34", "35-49", "50-64", "65+"], weights=[0.12, 0.28, 0.38, 0.22])[0]
    channel = random.choices(["Hospital", "Clinic", "Pharmacy"], weights=[0.25, 0.45, 0.30])[0]
    patient_rows.append([f"PT{i+1:06d}", age_band, condition, product_name, doctor.doctor_id, doctor.region, doctor.state, start_date.strftime("%Y-%m-%d"), status, round(adherence, 3), channel])

patients = pd.DataFrame(patient_rows, columns=["patient_id", "age_band", "condition", "product_name", "doctor_id", "region", "state", "therapy_start_date", "therapy_status", "adherence_rate", "channel"])

products.to_csv(RAW / "products.csv", index=False)
doctors.to_csv(RAW / "doctors.csv", index=False)
reps.to_csv(RAW / "sales_reps.csv", index=False)
sales.to_csv(RAW / "commercial_sales.csv", index=False)
patients.to_csv(RAW / "patient_reach.csv", index=False)

print(f"Generated {len(sales):,} commercial records and {len(patients):,} patient records in {RAW}")
