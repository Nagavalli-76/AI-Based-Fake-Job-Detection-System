import pandas as pd

# Load dataset
df = pd.read_csv("fake_job_postings.csv")

# Show first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())