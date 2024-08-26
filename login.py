import streamlit as st

USERS = {
    "usuario1": "password1",
    "usuario2": "password2",
}


def login():
    st.markdown("<h1 style='text-align: center;'>HelPharma</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.write("##")  # Espacio vertical
        st.markdown("#### Iniciar sesión", unsafe_allow_html=True)
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        login_button = st.button("Ingresar", use_container_width=True)

        if login_button:
            if username in USERS and USERS[username] == password:
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos")

        st.write("---")  # Línea divisoria
        st.markdown("<p style='text-align: center;'>¿No tienes una cuenta? <a href='#'>Regístrate</a></p>",
                    unsafe_allow_html=True)

    # Espacio vertical al final
    st.write("##")