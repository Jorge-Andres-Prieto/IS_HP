import streamlit as st
from streamlit_option_menu import option_menu
from login import login
from leer_archivo import main_program

# Configuración del tema
st.set_page_config(layout="wide", page_title="HelPharma")

# Aplicar el tema manualmente
st.markdown("""
    <style>
    :root {
        --primary-color: #008fc4;
        --background-color: #003041;
        --secondary-background-color: #ff0202;
        --text-color: #fcfdff;
        --font: sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def logout():
    st.session_state['logged_in'] = False
    st.session_state['username'] = None
    st.rerun()

def main_menu(user):
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["Home", "Excel"],
            icons=["house", "file-earmark-excel"],
            menu_icon="list",
            default_index=0
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