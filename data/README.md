# Data

The full raw datasets are generated locally by running:

```bash
python python/generate_synthetic_data.py
```

This creates:
- `data/raw/products.csv`
- `data/raw/doctors.csv`
- `data/raw/sales_reps.csv`
- `data/raw/commercial_sales.csv`
- `data/raw/patient_reach.csv`

The generated dataset is fully synthetic and contains no real patient data or protected health information.

The project generator creates approximately 9,846 commercial activity records, 350 doctors, 25 sales representatives, and 18,000 synthetic patient records.
