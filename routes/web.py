import streamlit as st
from routes import VisaoGeralController, OportunidadeController

def web_routes():
    page = st.sidebar.radio("Go to", ["Visão Geral", "Oportunidades"])

    if page == "Visão Geral":
        VisaoGeralController().index()

    if page == "Oportunidades":
        OportunidadeController().index()
