import streamlit as st


def show_kpi(title, value, subtitle):

    st.metric(
        label=title,
        value=value,
        help=subtitle
    )

    st.caption(subtitle)