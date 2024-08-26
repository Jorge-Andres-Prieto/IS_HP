import streamlit as st

USERS = {
    "usuario1": "password1",
    "usuario2": "password2",
}


def login():
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.title("HelPharma")
        st.write("##")  # Añade un espacio vertical

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Login", use_container_width=True)

        if login_button:
            if username in USERS and USERS[username] == password:
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.rerun()
            else:
                st.error("Username or password is incorrect")

    # Añadir un espacio vertical al final para empujar el contenido hacia arriba
    st.write("##")