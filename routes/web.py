import streamlit as st
from routes import home_controller, oportunidade_controller

def web_routes():
    page = st.sidebar.radio("Go to", ["Home", "Dashboard"])

    if page == "Home":
        home_controller()

    if page == "Dashboard":
        oportunidade_controller()