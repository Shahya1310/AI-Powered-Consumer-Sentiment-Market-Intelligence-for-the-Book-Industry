import streamlit as st
from utils.auth import signup
from theme import dark_theme

st.set_page_config(layout="centered")
dark_theme()

st.markdown("""
<style>
section[data-testid="stSidebar"] {display: none;}
button[aria-label="Menu"] {display: none;}
header {visibility: hidden;}

/* ---------- SELECTBOX HARD FIX ---------- */

/* main select container */
div[data-testid="stSelectbox"] > div {
    background: #111827 !important;
    border: 1px solid #374151 !important;
    border-radius: 12px !important;
}

/* selected value inside box */
div[data-testid="stSelectbox"] span {
    color: #000000 !important;
    opacity: 1 !important;
    -webkit-text-fill-color: #000000 !important;
}

/* dropdown panel */
div[role="listbox"] {
    background: #111827 !important;
}

/* dropdown options text (THIS is the real fix) */
div[role="option"] span {
    color: #000000 !important;
    opacity: 1 !important;
    -webkit-text-fill-color: #000000 !important;
}

/* hover */
div[role="option"]:hover span {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
}

/* remove focus ring */
*:focus {
    outline: none !important;
    box-shadow: none !important;
}

/* --------------------------------------- */
</style>
""", unsafe_allow_html=True)


st.title("Signup")

username = st.text_input("Create Username")
password = st.text_input("Create Password", type="password")

persona = st.selectbox(
    "Select Persona",
    ["Store Manager", "Regional Manager", "Executive"]
)

if st.button("Create Account"):
    if not username or not password:
        st.error("Fill all fields")
    else:
        ok = signup(username, password, persona)

        if ok:
            st.success("Account created! Please login.")
            st.switch_page("pages/Login.py")
        else:
            st.error("Username already exists")

if st.button("Back to Login"):
    st.switch_page("pages/Login.py")
