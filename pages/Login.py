import streamlit as st
from utils.auth import login
from theme import dark_theme

st.set_page_config(layout="centered")
dark_theme()

# hide Streamlit chrome only
st.markdown("""
<style>
section[data-testid="stSidebar"] {display: none;}
button[aria-label="Menu"] {display: none;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("Login")

u = st.text_input("Username")
p = st.text_input("Password", type="password")

if st.button("Login"):
    role = login(u, p)

    if role:
        st.session_state.user = u
        st.session_state.persona = role
        st.switch_page("pages/Overview.py")
    else:
        st.error("Invalid credentials")

if st.button("Create new account"):
    st.switch_page("pages/Signup.py")
