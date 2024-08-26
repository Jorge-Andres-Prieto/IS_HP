import streamlit as st
from login import login
from leer_archivo import main_program  # Importa tu programa principal

# Inicializa el estado de sesión al iniciar
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def main():
    if not st.session_state['logged_in']:
        login()
    else:
        with st.sidebar:
            selected = st.selectbox(
                "HelPharma",
                ["Home", "Excel"],
                index=0
            )
            if st.button("Cerrar Sesión"):
                st.session_state['logged_in'] = False

        if selected == "Home":
            st.write("Bienvenido a HelPharma")
        elif selected == "Excel":
            main_program()

if __name__ == "__main__":
    main()
