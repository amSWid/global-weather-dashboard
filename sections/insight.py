import streamlit as st
import pandas as pd

from components.charts import (
    bar_chart,
    scatter_chart,
    pie_chart
)


def show_insight(df):

    # =====================================
    # PAGE TITLE
    # =====================================

    st.markdown("""
        <div style="
        text-align:center;
        padding-top:10px;
        padding-bottom:15px;
    ">

    <h1 style="
    font-size:48px;
    font-weight:800;
    margin-bottom:0px;
    color:white;
    ">
    💡 Insight 
            
    </h1>

    <p style="
    font-size:18px;
    color:#B8C1EC;
    margin-top:8px;
    letter-spacing:1px;
    ">
    By S.Widjaja
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =====================================
    # OUTDOOR SCORE
    # =====================================

    df = df.copy()

    df["outdoor_score"] = (
        100
        - abs(df["temperature_celsius"] - 24) * 2
        - df["humidity"] * 0.2
        - df["uv_index"] * 1.5
        - df["air_quality_PM2.5"] * 0.3
    )

    # =====================================
    # FILTERS
    # =====================================

    st.markdown("## 🎯 Insight Filters")

    f1, f2, f3 = st.columns(3)

    with f1:

        selected_continent = st.selectbox(
            "Continent",
            ["All"] +
            sorted(
                df["continent"]
                .dropna()
                .unique()
            )
        )

    with f2:

        selected_country = st.selectbox(
            "Country",
            ["All"] +
            sorted(
                df["country"]
                .dropna()
                .unique()
            )
        )

    with f3:

        selected_condition = st.selectbox(
            "Weather",
            ["All"] +
            sorted(
                df["condition_text"]
                .dropna()
                .unique()
            )
        )

    filtered = df.copy()

    if selected_continent != "All":

        filtered = filtered[
            filtered["continent"]
            == selected_continent
        ]

    if selected_country != "All":

        filtered = filtered[
            filtered["country"]
            == selected_country
        ]

    if selected_condition != "All":

        filtered = filtered[
            filtered["condition_text"]
            == selected_condition
        ]

    # =====================================
    # EMPTY CHECK
    # =====================================

    if filtered.empty:

        st.warning(
            "No data available."
        )

        return

    st.divider()

    # =====================================
    # SECTION TITLE
    # =====================================

    st.markdown("""
    ## 🌍 Environmental Intelligence Analytics
    """)

    st.caption("""
    Environmental patterns and atmospheric
    indicators across global regions.
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================
    # ROW 1
    # =====================================

    c1, c2, c3 = st.columns(3)

    # =====================================
    # CHART 1
    # OUTDOOR SCORE
    # =====================================

    best_country = (
        filtered
        .groupby("country")[
            "outdoor_score"
        ]
        .mean()
        .sort_values(
            ascending=False
        )
        .head(10)
        .reset_index()
    )

    with c1:

        st.markdown("""
        ### 🌿 Best Outdoor Countries
        """)

        st.caption("""
        Higher outdoor scores indicate
        more comfortable environmental
        conditions with balanced temperature,
        humidity, pollution and UV exposure.
        """)

        bar_chart(
            best_country,
            x="outdoor_score",
            y="country",
            title="Outdoor Score"
        )

    # =====================================
    # CHART 2
    # POLLUTION
    # =====================================

    pollution = (
        filtered
        .groupby("country")[
            "air_quality_PM2.5"
        ]
        .mean()
        .sort_values(
            ascending=False
        )
        .head(10)
        .reset_index()
    )

    with c2:

        st.markdown("""
        ### 🌫 Pollution Ranking
        """)

        st.caption("""
        PM2.5 represents fine particulate
        pollution that may affect
        atmospheric quality and public health.
        """)

        bar_chart(
            pollution,
            x="air_quality_PM2.5",
            y="country",
            title="PM2.5"
        )

    # =====================================
    # CHART 3
    # UV
    # =====================================

    uv_data = (
        filtered
        .groupby("continent")[
            "uv_index"
        ]
        .mean()
        .reset_index()
    )

    with c3:

        st.markdown("""
        ### ☀ UV by Continent
        """)

        st.caption("""
        UV exposure levels vary across
        continents and may indicate
        differences in atmospheric intensity
        and sunlight exposure.
        """)

        bar_chart(
            uv_data,
            x="uv_index",
            y="continent",
            title="UV Index"
        )

    st.divider()

    # =====================================
    # SECTION TITLE
    # =====================================

    st.markdown("""
    ## 🌦 Atmospheric & Climate Patterns
    """)

    st.caption("""
    Weather comfort and atmospheric
    condition monitoring.
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================
    # ROW 2
    # =====================================

    c4, c5, c6 = st.columns(3)

    # =====================================
    # CHART 4
    # HUMIDITY
    # =====================================

    humidity_data = (
        filtered
        .groupby("continent")[
            "humidity"
        ]
        .mean()
        .reset_index()
    )

    with c4:

        st.markdown("""
        ### 💧 Humidity
        """)

        st.caption("""
        Humidity influences perceived
        weather comfort and atmospheric
        moisture conditions across regions.
        """)

        bar_chart(
            humidity_data,
            x="humidity",
            y="continent",
            title="Humidity"
        )

    # =====================================
    # CHART 5
    # WIND
    # =====================================

    wind_data = (
        filtered
        .groupby("country")[
            "wind_kph"
        ]
        .mean()
        .sort_values(
            ascending=False
        )
        .head(10)
        .reset_index()
    )

    with c5:

        st.markdown("""
        ### 🌬 Wind Speed
        """)

        st.caption("""
        Strong wind patterns may reflect
        dynamic atmospheric movement
        and changing climate behavior.
        """)

        bar_chart(
            wind_data,
            x="wind_kph",
            y="country",
            title="Wind Speed"
        )

    # =====================================
    # CHART 6
    # WEATHER CONDITION
    # =====================================

    weather_data = (
        filtered["condition_text"]
        .value_counts()
        .head(8)
        .reset_index()
    )

    weather_data.columns = [
        "condition",
        "count"
    ]

    with c6:

        st.markdown("""
        ### 🌦 Weather Condition
        """)

        st.caption("""
        Weather condition distribution
        provides insight into dominant
        atmospheric patterns within
        the selected regions.
        """)

        pie_chart(
            weather_data,
            names="condition",
            values="count",
            title="Condition Distribution"
        )

    st.divider()

    # =====================================
    # SECTION TITLE
    # =====================================

    st.markdown("""
    ## 🔥 Climate Relationship Analysis
    """)

    st.caption("""
    Relationships between pollution,
    temperature and atmospheric variables.
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================
    # ROW 3
    # =====================================

    c7, c8 = st.columns(2)

    # =====================================
    # CHART 7
    # SCATTER MATRIX
    # =====================================

    with c7:

        st.markdown("""
        ### 🌍 Climate Matrix
        """)

        st.caption("""
        The climate matrix visualizes
        relationships between temperature,
        pollution and humidity.

        Larger bubbles indicate regions
        with higher atmospheric moisture.
        """)

        scatter_chart(
            filtered,
            x="temperature_celsius",
            y="air_quality_PM2.5",
            color="continent",
            size="humidity",
            title="Climate Matrix"
        )

    # =====================================
    # CHART 8
    # ANOMALY DISTRIBUTION
    # =====================================

    anomaly_data = (
        filtered["anomaly"]
        .value_counts()
        .reset_index()
    )

    anomaly_data.columns = [
        "status",
        "count"
    ]

    anomaly_data["status"] = (
        anomaly_data["status"]
        .replace({
            1: "Normal",
            -1: "Anomaly"
        })
    )

    with c8:

        st.markdown("""
        ### 🚨 Climate Risk Distribution
        """)

        st.caption("""
        Climate anomalies represent
        unusual environmental conditions
        detected from atmospheric
        and pollution indicators.
        """)

        pie_chart(
            anomaly_data,
            names="status",
            values="count",
            title="Anomaly Distribution"
        )

    st.divider()

    # =====================================
    # SUMMARY
    # =====================================

    st.success(f"""
### 📌 Environmental Intelligence Summary

Dataset analyzed : {len(filtered):,} records

Key findings:

• Best outdoor locations show balanced environmental conditions

• PM2.5 remains one of the strongest pollution indicators

• UV exposure differs significantly across continents

• Humidity and wind patterns influence climate comfort

• Weather distributions reveal regional atmospheric behavior

• Climate anomalies indicate unusual environmental conditions

• Environmental intelligence supports sustainability awareness
""")

    # =====================================
    # DISCLAIMER
    # =====================================

    st.divider()

    st.info("""
### 📘 Environmental Insight Disclaimer

Environmental insights and outdoor scores
are generated from analytical calculations
using climate and atmospheric variables.

The results are intended for educational,
visualization and exploratory analytics purposes only.

Environmental comfort, pollution exposure
and climate interpretations may vary across regions
and should not replace official environmental reports.
""")