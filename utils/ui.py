import streamlit as st

def kpi_card(title, value, color="#6C63FF"):
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, {color}, #0f172a);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        animation: fadeIn 0.8s ease-in-out;
        box-shadow: 0px 4px 25px rgba(0,0,0,0.4);
    ">
        <h4>{title}</h4>
        <h2>{value}</h2>
    </div>

    <style>
    @keyframes fadeIn {{
        from {{opacity: 0; transform: translateY(20px);}}
        to {{opacity: 1; transform: translateY(0);}}
    }}
    </style>
    """, unsafe_allow_html=True)
