import streamlit as st
from streamlit_option_menu import option_menu
from login import login
from leer_archivo import main_program

# Inicializar estado de sesión
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def logout():
    st.session_state['logged_in'] = False
    st.session_state['username'] = None
    st.rerun()

def main_menu(user):
    with st.sidebar:
        selected = option_menu(
            menu_title="HelPharma",
            options=["Home", "Excel"],
            icons=["house-fill", "file-earmark-excel-fill"],  # Iconos para las opciones
            menu_icon="capsule",  # Icono para el título
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )
        if st.button("Cerrar Sesión"):
            logout()

    if selected == "Home":
        st.write("Bienvenido a HelPharma")
    elif selected == "Excel":
        main_program()

def main():
    if not st.session_state['logged_in']:
        login()
    else:
        main_menu(st.session_state['username'])

if __name__ == "__main__":
    main()
