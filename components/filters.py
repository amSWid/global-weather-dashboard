import streamlit as st


def show_filters(df):

    st.markdown(
        """
        <div class='section-title'>
        🔎 Explore Weather by Location
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        country = st.selectbox(
            "Choose Country",
            ["All"]
            + sorted(
                df["country"]
                .unique()
            )
        )

    with col2:
        city = st.selectbox(
            "Choose City",
            ["All"]
            + sorted(
                df["location_name"]
                .unique()
            )
        )

    st.markdown("### 🌍 Continent")

    continent = st.radio(
        "",
        [
            "All",
            "Asia",
            "Europe",
            "Africa",
            "North America",
            "South America",
            "Oceania"
        ],
        horizontal=True
    )

    filtered_df = df.copy()

    if country != "All":
        filtered_df = (
            filtered_df[
                filtered_df[
                    "country"
                ] == country
            ]
        )

    if city != "All":
        filtered_df = (
            filtered_df[
                filtered_df[
                    "location_name"
                ] == city
            ]
        )

    if continent != "All":
        filtered_df = (
            filtered_df[
                filtered_df[
                    "continent"
                ] == continent
            ]
        )

    return filtered_df