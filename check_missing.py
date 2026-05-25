import pandas as pd

# load dataset
df = pd.read_csv(
    "data/Global_Weather_Clean.csv"
)

print("Dataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isna().sum())