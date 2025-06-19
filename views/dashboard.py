import streamlit as st

def dashboard_page(data):
    st.title("Dashboard")
    st.write("### User Data")
    st.dataframe(data)
