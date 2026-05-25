import pandas as pd

# ====================================
# LOAD RAW DATASET
# ====================================

raw_df = pd.read_csv(
    "data/Global_Weather.csv"
)

# ====================================
# LOAD CLEAN DATASET
# ====================================

clean_df = pd.read_csv(
    "data/Global_Weather_Clean_v2.csv"
)

# ====================================
# DATASET SHAPE
# ====================================

print("\n" + "=" * 50)
print("RAW DATASET SHAPE")
print("=" * 50)

print(raw_df.shape)

print("\n" + "=" * 50)
print("CLEAN DATASET SHAPE")
print("=" * 50)

print(clean_df.shape)

# ====================================
# DATA TYPES
# ====================================

print("\n" + "=" * 50)
print("CLEAN DATA TYPES")
print("=" * 50)

print(clean_df.dtypes)

# ====================================
# MISSING VALUES
# ====================================

print("\n" + "=" * 50)
print("CLEAN MISSING VALUES")
print("=" * 50)

print(clean_df.isnull().sum())

# ====================================
# DUPLICATE ROWS
# ====================================

print("\n" + "=" * 50)
print("CLEAN DUPLICATES")
print("=" * 50)

print(clean_df.duplicated().sum())


##Check data extreme values

# ====================================
# WEATHER STATISTICS AUDIT
# ====================================

weather_cols = [
    "temperature_celsius",
    "humidity",
    "wind_kph",
    "pressure_mb",
    "uv_index",
    "air_quality_PM2.5",
    "latitude",
    "longitude"
]

print("\n" + "=" * 70)
print("WEATHER STATISTICS AUDIT")
print("=" * 70)

summary = clean_df[
    weather_cols
].describe().T[
    ["min", "mean", "max"]
]

print(summary.round(2))

# ====================================
# EXTREME VALUE CHECK
# ====================================

print("\n" + "=" * 70)
print("EXTREME WIND VALUES")
print("=" * 70)

print(
    clean_df.loc[
        clean_df["wind_kph"] > 400,
        [
            "country",
            "location_name",
            "wind_kph"
        ]
    ].head(20)
)

## ada data aneh di wind dan prssure :

print("\n" + "=" * 70)
print("EXTREME PRESSURE VALUES")
print("=" * 70)

print(
    clean_df.loc[
        clean_df["pressure_mb"] > 1100,
        [
            "country",
            "location_name",
            "pressure_mb"
        ]
    ].head(20)
)

print("\n" + "=" * 70)
print("EXTREME PM2.5 VALUES")
print("=" * 70)

print(
    clean_df.loc[
        clean_df[
            "air_quality_PM2.5"
        ] > 500,
        [
            "country",
            "location_name",
            "air_quality_PM2.5"
        ]
    ].head(20)
)


## re audit setelah perbaikan di temperatur dll 


print(df.shape)
print(df.isna().sum())