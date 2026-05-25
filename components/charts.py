# ====================================
# IMPORT LIBRARIES
# ====================================

import plotly.express as px
import streamlit as st


# ====================================
# GLOBAL COLOR PALETTE
# ====================================

CONTINENT_COLORS = {
    "Asia": "#FF6B6B",
    "Europe": "#4D96FF",
    "Africa": "#FFD93D",
    "North America": "#6BCB77",
    "South America": "#FF8E3C",
    "Oceania": "#B983FF"
}


# ====================================
# BASE LAYOUT
# ====================================

def apply_layout(fig, height=450):

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="white",
            family="Inter",
            size=13
        ),

        title=dict(
            x=0.02,
            xanchor="left",
            font=dict(
                size=20
            )
        ),

        height=height,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        legend=dict(

            title="",

            orientation="h",

            yanchor="bottom",
            y=1.02,

            xanchor="right",
            x=1,

            bgcolor="rgba(0,0,0,0)",

            font=dict(
                size=12
            )
        ),

        hoverlabel=dict(
            bgcolor="#111827",
            font_size=13,
            font_family="Inter"
        )
    )

    return fig


# ====================================
# WORLD MAP
# ====================================

def world_map(df):

    fig = px.scatter_geo(

        df,

        lat="latitude",
        lon="longitude",

        color="temperature_celsius",

        size="humidity",

        hover_name="location_name",

        hover_data={
            "country": True,
            "temperature_celsius": ":.1f",
            "humidity": ":.1f",
            "air_quality_PM2.5": ":.1f",
            "latitude": False,
            "longitude": False
        },

        labels={
            "temperature_celsius": "Temperature °C",
            "humidity": "Humidity %",
            "air_quality_PM2.5": "PM2.5"
        },

        projection="orthographic",

        color_continuous_scale="Turbo"
    )

    # ====================================
    # MARKER STYLE
    # ====================================

    fig.update_traces(

        marker=dict(

            opacity=0.85,

            line=dict(
                width=0.5,
                color="white"
            )
        )
    )

    # ====================================
    # GEO STYLE
    # ====================================

    fig.update_geos(

        bgcolor="rgba(0,0,0,0)",

        showland=True,
        landcolor="#16324F",

        showocean=True,
        oceancolor="#071018",

        showcountries=True,
        countrycolor="rgba(255,255,255,0.15)",

        showcoastlines=True,
        coastlinecolor="rgba(255,255,255,0.2)",

        projection_scale=1
    )

    # ====================================
    # COLORBAR LEGEND
    # ====================================

    fig.update_layout(

        height=700,

        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),

        paper_bgcolor="rgba(0,0,0,0)",

        coloraxis_colorbar=dict(

            title="🌡 Temperature °C",

            thickness=18,

            len=0.7,

            tickfont=dict(
                size=11
            )
        )
    )

    # ====================================
    # SHOW CHART
    # ====================================

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ====================================
    # GLOBE LEGEND
    # ====================================

    st.caption("""
🌍 Globe Color Legend

🔵 Blue → Cooler temperature regions

🟢 Green → Moderate climate conditions

🟡 Yellow → Warm temperature zones

🔴 Red → High temperature hotspots

Bubble size represents humidity intensity across locations.
""")


# ====================================
# LINE CHART
# ====================================

def line_chart(
    df,
    x,
    y,
    color=None,
    title=""
):

    fig = px.line(

        df,

        x=x,
        y=y,

        color=color,

        title=title,

        color_discrete_map=CONTINENT_COLORS,

        labels={
            x: x.replace("_", " ").title(),
            y: y.replace("_", " ").title(),
            color: "Continent"
        }
    )

    fig.update_traces(
        line=dict(width=3)
    )

    fig = apply_layout(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ====================================
# BAR CHART
# ====================================

def bar_chart(
    df,
    x,
    y,
    title=""
):

    fig = px.bar(

        df,

        x=x,
        y=y,

        orientation="h",

        title=title,

        color=x,

        color_continuous_scale="Turbo",

        labels={
            x: x.replace("_", " ").title(),
            y: y.replace("_", " ").title()
        }
    )

    fig.update_layout(

        coloraxis_colorbar=dict(
            title=x.replace("_", " ").title()
        )
    )

    fig = apply_layout(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ====================================
# SCATTER CHART
# ====================================

def scatter_chart(
    df,
    x,
    y,
    color=None,
    size=None,
    title=""
):

    fig = px.scatter(

        df,

        x=x,
        y=y,

        color=color,

        size=size,

        title=title,

        opacity=0.78,

        color_discrete_map=CONTINENT_COLORS,

        labels={
            x: x.replace("_", " ").title(),
            y: y.replace("_", " ").title(),
            color: "🌍 Continent",
            size: "💧 Intensity"
        },

        hover_data={
            x: ":.1f",
            y: ":.1f"
        }
    )

    fig.update_traces(

        marker=dict(

            line=dict(
                width=1,
                color="white"
            )
        )
    )

    fig.update_layout(

        legend=dict(
            title="🌍 Continent"
        )
    )

    fig = apply_layout(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ====================================
# PIE CHART
# ====================================

def pie_chart(
    df,
    names,
    values,
    title=""
):

    fig = px.pie(

        df,

        names=names,

        values=values,

        title=title,

        hole=0.6,

        color_discrete_sequence=px.colors.qualitative.Bold
    )

    fig.update_traces(

        textinfo="percent+label",

        textfont_size=13,

        pull=[0.03] * len(df)
    )

    fig = apply_layout(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )