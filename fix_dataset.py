import pandas as pd

# ====================================
# LOAD CLEAN DATASET
# ====================================

df = pd.read_csv(
    "data/Global_Weather_Clean.csv"
)

print("\nDataset Loaded")
print(df.shape)

# ====================================
# FIX PRESSURE TYPO
# ====================================

print("\nFixing Pressure Values...")

df.loc[
    df["pressure_mb"] == 3006,
    "pressure_mb"
] = 1006

df.loc[
    df["pressure_mb"] == 3000,
    "pressure_mb"
] = 1000

# ====================================
# CAP EXTREME WIND SPEED
# Using 180 kph as a reasonable upper limit for wind speed based on historical weather data
# ====================================

print("\nCapping Extreme Wind...")

wind_cap = 180

print(
    f"Wind Cap Threshold: {wind_cap}"
)

df["wind_kph"] = (
    df["wind_kph"]
    .clip(upper=wind_cap)
)

# ====================================
# FINAL VALIDATION
# ====================================

print("\nValidation Check")

print(
    "Max Wind:",
    df["wind_kph"].max()
)

print(
    "Max Pressure:",
    df["pressure_mb"].max()
)

# ====================================
# SAVE NEW FILE
# ====================================

output_path = (
    "data/Global_Weather_Clean_v2.csv"
)

df.to_csv(
    output_path,
    index=False
)

print("\nNew File Saved:")
print(output_path)

