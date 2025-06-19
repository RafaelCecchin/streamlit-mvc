import streamlit as st

def view(data):
    st.title("Dashboard")
    st.write("### User Data")
    st.dataframe(data)
