import pandas as pd
import streamlit as st


@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/Global_Weather_Clean_v2.csv"
    )

    # ==================================
    # DATE PROCESSING
    # ==================================

    if "last_updated" in df.columns:

        df["last_updated"] = pd.to_datetime(
            df["last_updated"],
            errors="coerce"
        )

        df["year"] = (
            df["last_updated"]
            .dt.year
        )

        df["month"] = (
            df["last_updated"]
            .dt.strftime("%b")
        )

    # ==================================
    # NUMERIC CLEANING
    # ==================================

    numeric_cols = [
        "temperature_celsius",
        "humidity",
        "wind_kph",
        "pressure_mb",
        "uv_index",
        "air_quality_PM2.5",
        "latitude",
        "longitude"
    ]

    for col in numeric_cols:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    # ==================================
    # TEXT CLEANING
    # ==================================

    for col in [
        "country",
        "continent",
        "location_name"
    ]:

        if col in df.columns:

            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
            )

    return df