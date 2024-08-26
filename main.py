import streamlit as st
from login import login_page
from leer_archivo import main_program

# Comprueba si el usuario ha iniciado sesión
if 'user' not in st.session_state:
    login_page()
else:
    with st.sidebar:
        selected = st.selectbox(
            "HelPharma",
            ["Home", "Excel"],
            index=0
        )
        if st.button("Cerrar Sesión"):
            del st.session_state['user']
            st.experimental_rerun()

    if selected == "Home":
        st.write("Bienvenido a HelPharma")
    elif selected == "Excel":
        main_program()
