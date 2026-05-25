import streamlit as st


def metric_card(
    title,
    value,
    delta=None
):

    st.metric(
        title,
        value,
        delta=delta
    )