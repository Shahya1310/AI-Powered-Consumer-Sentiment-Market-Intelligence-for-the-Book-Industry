import streamlit as st
from utils.session import init_session
from theme import dark_theme

dark_theme()
init_session()
st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.markdown("""
<style>

/* Kill Streamlit sidebar completely */
section[data-testid="stSidebar"] {
    display: none !important;
}

/* Remove Streamlit's center wrapper */
.block-container {
    max-width: 100% !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
}

/* Force full-width app */
.stApp {
    margin: 0 !important;
    padding: 0 !important;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Landing Page
# -----------------------------

st.markdown("""
<div style="text-align:center; margin-top:80px;">

<h1 style="font-size:48px;">📊 AI Market Intelligence Platform</h1>

<p style="font-size:20px; color:#cbd5f5; margin-top:20px;">
An AI-powered analytics dashboard that transforms customer feedback
into actionable business insights.
</p>

<p style="font-size:18px; color:#9ca3af; max-width:700px; margin:auto; margin-top:10px;">
Explore sentiment trends, emerging topics, and executive summaries
through Retrieval-Augmented Generation (RAG). Designed for Store Managers,
Regional Leaders, and Executives to make smarter data-driven decisions.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

# -----------------------------
# Buttons Row
# -----------------------------

col1, col2, col3 = st.columns([1,2,1])

with col2:
    c1, c2 = st.columns(2)

    with c1:
        if st.button("Login", use_container_width=True):
            st.switch_page("pages/Login.py")

    with c2:
        if st.button("Signup", use_container_width=True):
            st.switch_page("pages/Signup.py")
