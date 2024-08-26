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
            menu_title=None,  # Quitamos el título del menú
            options=["Home", "Excel"],
            icons=["house-door", "file-earmark-spreadsheet"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "#0096c7", "font-size": "25px"},
                "nav-link": {
                    "font-size": "18px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                    "font-weight": "normal",
                },
                "nav-link-selected": {"background-color": "#0096c7", "color": "white"},
            }
        )

        st.sidebar.markdown("---")
        if st.sidebar.button("Cerrar Sesión", key="logout"):
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
