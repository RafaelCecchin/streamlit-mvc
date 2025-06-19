import streamlit as st
from models.data_loader import load_data

# Views
from views.home import home_page
from views.dashboard import dashboard_page

def app_controller():
    # Controls app navigation and logic.
    
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Dashboard"])
    
    if page == "Home":
        home_page()

    if page == "Dashboard":
        data = load_data()
        dashboard_page(data)