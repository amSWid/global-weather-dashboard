import streamlit as st

from load_data import load_data

from components.styling import apply_global_style
from components.navbar import show_navbar

from sections.overview import show_overview
from sections.anomaly import show_anomaly
from sections.insight import show_insight


# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Global Weather Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================
# GLOBAL STYLE
# =========================================

apply_global_style()

# =========================================
# LOAD DATA
# =========================================

@st.cache_data
def get_data():
    return load_data()

df = get_data()

# =========================================
# NAVIGATION
# =========================================

selected_page = show_navbar()

# =========================================
# PAGE ROUTER
# =========================================

page_router = {
    "Overview": show_overview,
    "Anomaly": show_anomaly,
    "Insight": show_insight
}

page_router[selected_page](df)