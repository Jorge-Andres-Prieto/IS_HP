import streamlit as st

# Datos de usuarios y contraseñas (puedes cambiarlo a leer desde secrets)
USERS = {
    "usuario1": "password1",
    "usuario2": "password2",
}

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
        else:
            st.error("Username or password is incorrect")
