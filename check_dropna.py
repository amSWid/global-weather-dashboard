import pandas as pd

# load raw dataset
df_clean = pd.read_csv(
    "data/Global_Weather.csv"
)

print("Before dropna:")
print(df_clean.shape)

# remove missing values
df_clean = df_clean.dropna()

print("After dropna:")
print(df_clean.shape)

print("\nMissing values after cleaning:")
print(df_clean.isnull().sum())
