import pandas as pd

# Load dataset
df = pd.read_csv('uber.csv') # Replace with your file name

# Look at first rows
print(df.head())

# Check structure
print(df.info())

# Basic stats
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values (or handle as needed)
df_clean = df.dropna()

# Save cleaned data
df_clean.to_csv('UberDataset_Clean.csv', index=False)
