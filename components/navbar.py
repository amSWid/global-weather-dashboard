import streamlit as st


def show_navbar():

    st.markdown(
        """
        <h1 style="
            text-align:center;
            font-size:52px;
            font-weight:800;
            margin-bottom:8px;
        ">
            GLOBAL WEATHER DASHBOARD
        </h1>

        <div style="
            text-align:center;
            font-size:18px;
            color:#94A3B8;
            margin-bottom:30px;
        ">
            Atmospheric & Environmental Monitoring Platform
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns([1,1,1])

    if "page" not in st.session_state:
        st.session_state.page = "Overview"

    with c1:
        if st.button(
            "🌍 OVERVIEW",
            use_container_width=True
        ):
            st.session_state.page = "Overview"

    with c2:
        if st.button(
            "🚨 ANOMALY",
            use_container_width=True
        ):
            st.session_state.page = "Anomaly"

    with c3:
        if st.button(
            "💡 INSIGHT",
            use_container_width=True
        ):
            st.session_state.page = "Insight"

    st.divider()

    return st.session_state.page