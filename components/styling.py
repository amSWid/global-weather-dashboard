import streamlit as st


def apply_global_style():

    st.markdown("""
    <style>

    /* =================================
       GLOBAL
    ================================= */

    .stApp{

        background:
        linear-gradient(
        180deg,
        #071018 0%,
        #0B1622 100%
        );

        color:white;
    }

    html,
    body,
    [class*="css"]{

        font-family:
        Inter,
        sans-serif;
    }

    .block-container{

        max-width:1500px;

        padding-top:1.5rem;

        padding-left:2rem;

        padding-right:2rem;

        padding-bottom:2rem;
    }

    /* =================================
       HERO SECTION
    ================================= */

    .hero-wrapper{

        margin-bottom:24px;
    }

    .hero-badge{

        display:inline-block;

        background:
        rgba(56,189,248,0.12);

        border:
        1px solid rgba(56,189,248,0.25);

        color:#38BDF8;

        padding:
        8px 18px;

        border-radius:999px;

        font-size:12px;

        font-weight:700;

        letter-spacing:1px;

        margin-bottom:18px;
    }

    .hero-title{

        font-size:54px;

        font-weight:800;

        color:white;

        line-height:1.1;

        margin-bottom:12px;
    }

    .hero-subtitle{

        font-size:18px;

        color:#94A3B8;

        max-width:760px;

        line-height:1.7;
    }

    /* =================================
       NAVBAR
    ================================= */

    div[role="radiogroup"]{

    display:flex;

    justify-content:center !important;

    align-items:center;

    gap:14px;

    width:100%;

    margin-top:24px;

    margin-bottom:10px;
}

    div[role="radiogroup"] label{

        background:
        rgba(15,23,42,0.82);

        border:
        1px solid rgba(255,255,255,0.08);

        border-radius:14px;

        padding:
        12px 22px;

        transition:0.25s ease;

        min-width:140px;

        justify-content:center;
    }

    div[role="radiogroup"] label:hover{

        border:
        1px solid #38BDF8;

        transform:
        translateY(-2px);

        box-shadow:
        0px 0px 18px rgba(56,189,248,0.18);
    }

    /* =================================
       FILTER BOX
    ================================= */

    .filter-box{

        background:
        rgba(15,23,42,0.78);

        border:
        1px solid rgba(255,255,255,0.08);

        border-radius:24px;

        padding:24px;

        position:sticky;

        top:20px;
    }

    /* =================================
       METRIC CARD
    ================================= */

    div[data-testid="metric-container"]{

        background:
        rgba(15,23,42,0.75);

        border:
        1px solid rgba(255,255,255,0.08);

        padding:22px;

        border-radius:22px;

        box-shadow:
        0px 4px 20px rgba(0,0,0,0.2);
    }

    /* =================================
       CHART
    ================================= */

    div[data-testid="stPlotlyChart"]{

        background:
        rgba(15,23,42,0.55);

        border:
        1px solid rgba(255,255,255,0.08);

        border-radius:24px;

        padding:10px;
    }

    /* =================================
       TEXT
    ================================= */

    h1,
    h2,
    h3,
    h4{

        color:white !important;
    }

    p{

        color:#CBD5E1;
    }

    /* =================================
       MOBILE
    ================================= */

    @media (max-width:768px){

        .hero-title{
            font-size:36px;
        }

        .hero-subtitle{
            font-size:15px;
        }

        .block-container{

            padding-left:1rem;
            padding-right:1rem;
        }

        div[role="radiogroup"]{

            flex-wrap:wrap;
        }
    }

    </style>
    """, unsafe_allow_html=True)