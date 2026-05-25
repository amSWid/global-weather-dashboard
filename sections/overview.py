import streamlit as st

from components.cards import metric_card

from components.charts import (
    world_map,
    scatter_chart,
    bar_chart,
    pie_chart
)


def show_overview(df):

    # =====================================
    # COPY DATA
    # =====================================

    filtered_df = df.copy()

    # =====================================
    # PAGE HEADER
    # =====================================

    st.markdown("""
    <div style="
    text-align:center;
    padding-top:10px;
    padding-bottom:5px;
    ">

    <h1 style="
    font-size:52px;
    font-weight:800;
    margin-bottom:0px;
    color:white;
    ">
    🌍 Overview
    </h2>

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

    st.caption("""
    Global atmospheric analytics and environmental monitoring dashboard.
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================
    # DATA CLEANING SUMMARY
    # =====================================

    st.markdown("""
    ## 📂 Data Cleaning Summary
    """)

    raw_rows = 1_097_629
    clean_rows = len(df)
    removed_rows = raw_rows - clean_rows

    total_countries = (
        df["country"]
        .nunique()
    )

    total_continents = (
        df["continent"]
        .nunique()
    )

    total_cities = (
        df["location_name"]
        .nunique()
    )

    total_anomaly = len(
        df[
            df["anomaly"] == -1
        ]
    )

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:

        metric_card(
            "📂 Raw Dataset",
            f"{raw_rows:,}",
            "Original"
        )

    with kpi2:

        metric_card(
            "✅ Clean Dataset",
            f"{clean_rows:,}",
            "Processed"
        )

    with kpi3:

        metric_card(
            "🗑 Removed Rows",
            f"{removed_rows:,}",
            "Filtered"
        )

    with kpi4:

        metric_card(
            "🚨 Anomalies",
            f"{total_anomaly:,}",
            "Detected"
        )

    kpi5, kpi6, kpi7, kpi8 = st.columns(4)

    with kpi5:

        metric_card(
            "🌍 Countries",
            total_countries,
            "Coverage"
        )

    with kpi6:

        metric_card(
            "🏙 Cities",
            total_cities,
            "Locations"
        )

    with kpi7:

        metric_card(
            "🧭 Continents",
            total_continents,
            "Regions"
        )

    with kpi8:

        metric_card(
            "📊 Climate Data",
            f"{len(filtered_df):,}",
            "Records"
        )

    st.divider()

    # =====================================
    # MAIN SECTION
    # =====================================

    left, right = st.columns(
        [1, 3],
        gap="medium"
    )

    # =====================================
    # LEFT PANEL
    # =====================================

    with left:

        st.markdown("""
        ##  Dashboard Purpose
        """)

        st.caption("""
        Environmental intelligence dashboard
        for monitoring global climate,
        pollution and atmospheric conditions.
        """)

        st.markdown("""
🟢 Climate monitoring

🔵 Pollution analysis

🟣 Atmospheric intelligence

🟡 Environmental anomaly detection
""")

        st.divider()

        st.markdown("""
        ## 🔎 Climate Filters
        """)

        countries = ["All"] + sorted(
            filtered_df["country"]
            .dropna()
            .unique()
        )

        selected_country = st.selectbox(
            "Country",
            countries
        )

        continents = ["All"] + sorted(
            filtered_df["continent"]
            .dropna()
            .unique()
        )

        selected_continent = st.selectbox(
            "Continent",
            continents
        )

        anomaly_filter = st.selectbox(
            "Climate Condition",
            [
                "All",
                "Normal",
                "Anomaly"
            ]
        )

        st.divider()

        st.info("""
🌍 Global climate analytics

🌫 Air quality monitoring

☀ Environmental intelligence

🚨 Climate anomaly detection
""")

    # =====================================
    # FILTERING
    # =====================================

    if selected_country != "All":

        filtered_df = filtered_df[
            filtered_df["country"]
            == selected_country
        ]

    if selected_continent != "All":

        filtered_df = filtered_df[
            filtered_df["continent"]
            == selected_continent
        ]

    if anomaly_filter == "Normal":

        filtered_df = filtered_df[
            filtered_df["anomaly"] == 1
        ]

    elif anomaly_filter == "Anomaly":

        filtered_df = filtered_df[
            filtered_df["anomaly"] == -1
        ]

    # =====================================
    # EMPTY CHECK
    # =====================================

    if filtered_df.empty:

        st.warning(
            "No data available."
        )

        return

    # =====================================
    # RIGHT PANEL
    # =====================================

    with right:

        # =====================================
        # WEATHER SUMMARY
        # =====================================

        st.markdown("""
        ## 🌦 Global Weather Summary
        """)

        summary1, summary2, summary3, summary4 = st.columns(4)

        with summary1:

            metric_card(
                "🌡 Temperature",
                f"{round(filtered_df['temperature_celsius'].mean(),1)}°C",
                "Average"
            )

        with summary2:

            metric_card(
                "💧 Humidity",
                f"{round(filtered_df['humidity'].mean(),1)}%",
                "Atmosphere"
            )

        with summary3:

            metric_card(
                "🌫 PM2.5",
                round(
                    filtered_df[
                        "air_quality_PM2.5"
                    ].mean(),
                    1
                ),
                "Air Quality"
            )

        with summary4:

            metric_card(
                "☀️ UV Index",
                round(
                    filtered_df[
                        "uv_index"
                    ].mean(),
                    1
                ),
                "Environmental"
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # =====================================
        # GLOBAL GLOBE
        # =====================================

        st.markdown("""
        ## 🌎 Global Climate Globe
        """)

        st.caption("""
Interactive environmental globe showing
temperature intensity and humidity distribution.

🟣 Purple → Cold climate

🔵 Blue → Cool regions

🟢 Green → Moderate climate

🟡 Yellow → Warm regions

🔴 Red → Extreme heat zones

Bubble size represents humidity intensity.
""")

        world_map(filtered_df)

    st.divider()

    # =====================================
    # ROW 1
    # =====================================

    c1, c2 = st.columns(2)

    hottest = (
        filtered_df
        .groupby("country")[
            "temperature_celsius"
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
        ### 🔥 Hottest Countries
        """)

        st.caption("""
Countries with the highest
average temperature levels.
""")

        bar_chart(
            hottest,
            x="temperature_celsius",
            y="country",
            title="Average Temperature"
        )

    pollution = (
        filtered_df
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
Countries with elevated
PM2.5 pollution exposure.
""")

        bar_chart(
            pollution,
            x="air_quality_PM2.5",
            y="country",
            title="PM2.5"
        )

    # =====================================
    # ROW 2
    # =====================================

    c3, c4, c5 = st.columns(3)

    humidity_data = (
        filtered_df
        .groupby("continent")[
            "humidity"
        ]
        .mean()
        .reset_index()
    )

    with c3:

        st.markdown("""
        ### 💧 Humidity
        """)

        st.caption("""
Average atmospheric
humidity by continent.
""")

        bar_chart(
            humidity_data,
            x="humidity",
            y="continent",
            title="Humidity"
        )

    uv_data = (
        filtered_df
        .groupby("continent")[
            "uv_index"
        ]
        .mean()
        .reset_index()
    )

    with c4:

        st.markdown("""
        ### ☀️ UV Index
        """)

        st.caption("""
Average UV radiation
exposure across continents.
""")

        bar_chart(
            uv_data,
            x="uv_index",
            y="continent",
            title="UV Index"
        )

    condition_data = (
        filtered_df[
            "condition_text"
        ]
        .value_counts()
        .head(5)
        .reset_index()
    )

    condition_data.columns = [
        "condition",
        "count"
    ]

    with c5:

        st.markdown("""
        ### 🌦 Weather
        """)

        st.caption("""
Most common observed
weather conditions globally.
""")

        pie_chart(
            condition_data,
            names="condition",
            values="count",
            title="Conditions"
        )

    # =====================================
    # ROW 3
    # =====================================

    c6, c7, c8 = st.columns(3)

    wind_data = (
        filtered_df
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

    with c6:

        st.markdown("""
        ### 🌬 Wind Speed
        """)

        st.caption("""
Countries with stronger
average wind activity.
""")

        bar_chart(
            wind_data,
            x="wind_kph",
            y="country",
            title="Wind Speed"
        )

    anomaly_data = (
        filtered_df["anomaly"]
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

    with c7:

        st.markdown("""
        ### 🚨 Climate Anomaly
        """)

        st.caption("""
Detected unusual environmental
and atmospheric conditions.
""")

        pie_chart(
            anomaly_data,
            names="status",
            values="count",
            title="Anomaly Distribution"
        )

    with c8:

        st.markdown("""
        ### 📊 Climate Correlation
        """)

        st.caption("""
Relationship between temperature,
pollution and humidity.
""")

        scatter_chart(
            filtered_df,
            x="temperature_celsius",
            y="air_quality_PM2.5",
            color="continent",
            size="humidity",
            title="Climate Correlation"
        )

    st.divider()

    # =====================================
    # SUMMARY
    # =====================================

    st.success("""
### 📌 Climate Intelligence Summary

• Global temperature patterns vary significantly across continents

• PM2.5 remains one of the strongest pollution indicators

• Humidity and UV exposure influence environmental comfort

• Climate anomaly detection helps identify unusual weather conditions

• Environmental analytics support sustainability and monitoring
""")

    st.divider()

    # =====================================
    # DISCLAIMER
    # =====================================

    st.info("""
### ℹ Dashboard Disclaimer

This dashboard provides environmental
and weather analytics based on processed datasets.

Climate indicators including temperature,
humidity, pollution and UV exposure are displayed
for educational and analytical purposes only.

Values shown may not represent official
meteorological observations or real-time conditions.
""")