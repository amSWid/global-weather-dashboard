import streamlit as st

from components.cards import metric_card
from components.charts import (
    scatter_chart,
    bar_chart
)


def show_anomaly(df):

    # ====================================
    # FILTER ANOMALY
    # ====================================

    anomaly_df = df[
        df["anomaly"] == -1
    ]

    # ====================================
    # EMPTY CHECK
    # ====================================

    if anomaly_df.empty:

        st.warning(
            "No anomaly data available."
        )

        return

    # ====================================
    # CENTER HEADER
    # ====================================

    top1, top2, top3 = st.columns(
        [1, 2, 1]
    )

    with top2:

        st.markdown("""
        <h1 style='
            text-align:center;
            font-size:52px;
            font-weight:800;
            margin-bottom:0px;
        '>
        🚨 Climate Anomaly Center
        </h1>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p style='
            text-align:center;
            color:#B8C1EC;
            font-size:18px;
            margin-top:-10px;
            letter-spacing:1px;
        '>
        By S.Widjaja
        </p>
        """, unsafe_allow_html=True)

    st.caption("""
    Advanced environmental anomaly monitoring
    across continents using atmospheric,
    pollution and climate indicators.
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    # ====================================
    # KPI SECTION
    # ====================================

    col1, col2, col3, col4 = st.columns(4)

    total_anomaly = len(anomaly_df)

    avg_temp = round(
        anomaly_df["temperature_celsius"].mean(),
        1
    )

    avg_pm25 = round(
        anomaly_df["air_quality_PM2.5"].mean(),
        1
    )

    avg_humidity = round(
        anomaly_df["humidity"].mean(),
        1
    )

    with col1:

        metric_card(
            "⚠ Total Anomaly",
            f"{total_anomaly:,}",
            "Detected"
        )

    with col2:

        metric_card(
            "🌡 Avg Temperature",
            f"{avg_temp}°C",
            "Climate"
        )

    with col3:

        metric_card(
            "🌫 Avg PM2.5",
            avg_pm25,
            "Pollution"
        )

    with col4:

        metric_card(
            "💧 Avg Humidity",
            f"{avg_humidity}%",
            "Atmosphere"
        )

    st.divider()

    # ====================================
    # SECTION TITLE
    # ====================================

    st.markdown("""
    ## 🛰 Continental Climate Intelligence
    """)

    st.caption("""
    Environmental anomaly distribution
    across global continents.
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    # ====================================
    # ROW 1
    # ====================================

    c1, c2, c3 = st.columns(3)

    # ====================================
    # CHART 1
    # ====================================

    continent_risk = (
        anomaly_df
        .groupby("continent")
        .size()
        .reset_index(name="anomaly_count")
        .sort_values(
            "anomaly_count",
            ascending=False
        )
    )

    with c1:

        st.markdown("""
        ### 🚨 Anomaly Distribution
        """)

        st.caption("""
        Continents with higher anomaly counts
        indicate regions experiencing more
        unusual environmental conditions.
        """)

        bar_chart(
            continent_risk,
            x="anomaly_count",
            y="continent",
            title="Anomaly by Continent"
        )

    # ====================================
    # CHART 2
    # ====================================

    continent_temp = (
        anomaly_df
        .groupby("continent")[
            "temperature_celsius"
        ]
        .mean()
        .reset_index()
        .sort_values(
            "temperature_celsius",
            ascending=False
        )
    )

    with c2:

        st.markdown("""
        ### 🌡 Temperature Risk
        """)

        st.caption("""
        Unusual temperature levels may
        indicate atmospheric instability
        and climate irregularities.
        """)

        bar_chart(
            continent_temp,
            x="temperature_celsius",
            y="continent",
            title="Average Temperature"
        )

    # ====================================
    # CHART 3
    # ====================================

    continent_pm25 = (
        anomaly_df
        .groupby("continent")[
            "air_quality_PM2.5"
        ]
        .mean()
        .reset_index()
        .sort_values(
            "air_quality_PM2.5",
            ascending=False
        )
    )

    with c3:

        st.markdown("""
        ### 🌫 Pollution Exposure
        """)

        st.caption("""
        High PM2.5 concentrations indicate
        unhealthy environmental conditions
        and pollution anomalies.
        """)

        bar_chart(
            continent_pm25,
            x="air_quality_PM2.5",
            y="continent",
            title="Average PM2.5"
        )

    st.divider()

    # ====================================
    # HOTSPOT SECTION
    # ====================================

    st.markdown("""
    ## 🔥 Environmental Risk Hotspots
    """)

    st.caption("""
    Climate hotspot analysis based on
    atmospheric instability indicators.
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    # ====================================
    # ROW 2
    # ====================================

    c4, c5 = st.columns(
        [2, 1],
        gap="large"
    )

    # ====================================
    # CHART 4
    # ====================================

    with c4:

        st.markdown("""
        ### 🌍 Climate Hotspot Matrix
        """)

        st.caption("""
        Climate anomalies often emerge
        in regions with unusual combinations
        of temperature, humidity and pollution.
        """)

        scatter_chart(
            anomaly_df,
            x="temperature_celsius",
            y="humidity",
            color="continent",
            size="air_quality_PM2.5",
            title="Temperature vs Humidity"
        )

    # ====================================
    # CHART 5
    # ====================================

    uv_risk = (
        anomaly_df
        .groupby("continent")[
            "uv_index"
        ]
        .mean()
        .reset_index()
        .sort_values(
            "uv_index",
            ascending=False
        )
    )

    with c5:

        st.markdown("""
        ### ☀ UV Exposure Risk
        """)

        st.caption("""
        High UV exposure may indicate
        environmental stress conditions
        and atmospheric instability.
        """)

        bar_chart(
            uv_risk,
            x="uv_index",
            y="continent",
            title="Average UV Index"
        )

    st.divider()

    # ====================================
    # SUMMARY
    # ====================================

    st.success(f"""
### 📌 Climate Intelligence Summary

Dataset analyzed : {len(anomaly_df):,} anomaly records

Key findings:

• Climate anomalies are distributed unevenly across continents

• Temperature and pollution remain major environmental indicators

• UV exposure contributes to environmental stress

• Humidity and temperature relationships reveal climate hotspots

• Atmospheric anomaly monitoring supports climate awareness
""")

    # ====================================
    # DISCLAIMER
    # ====================================

    st.divider()

    st.warning("""
### ⚠ Anomaly Detection Disclaimer

Climate anomalies shown in this dashboard
are generated using statistical or machine
learning-based anomaly detection methods.

Detected anomalies represent unusual
environmental patterns compared to
general climate behavior within the dataset.

These results should not be interpreted
as official climate warnings or
certified environmental assessments.
""")