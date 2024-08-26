import streamlit as st

# Diccionario con los usuarios y contraseñas
USERS = {
    "usuario1": "password1",
    "usuario2": "password2",
}

def verify_user(username, password):
    if USERS.get(username) == password:
        return username
    return None

def login_page():
    st.title("HelPharma Login")
    username = st.text_input("Nombre de Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        user = verify_user(username, password)
        if user:
            st.session_state['user'] = user
            st.experimental_rerun()
        else:
            st.error("Usuario o contraseña incorrectos.")
