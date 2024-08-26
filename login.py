import streamlit as st

# Usuarios y contraseñas almacenados en un diccionario
USERS = {
    "usuario1": "password1",
    "usuario2": "password2",
}


def login():
    st.title("HelPharma Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if USERS.get(username) == password:
            st.session_state['logged_in'] = True
            st.success("Login successful")
        else:
            st.error("Incorrect username or password")
