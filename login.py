import streamlit as st

USERS = {
    "usuario1": "password1",
    "usuario2": "password2",
}

def login():
    st.set_page_config(layout="centered", page_title="HelPharma Login")

    st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
        font-weight: bold;
        color: #008fc4;
        text-align: center;
    }
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
    }
    .login-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">HelPharma</p>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="container">', unsafe_allow_html=True)
        with st.form("login_form"):
            st.markdown('<div class="login-box">', unsafe_allow_html=True)
            username = st.text_input("Usuario")
            password = st.text_input("Contraseña", type="password")
            submit_button = st.form_submit_button("Iniciar Sesión")

            if submit_button:
                if username in USERS and USERS[username] == password:
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = username
                    st.rerun()
                else:
                    st.error("Usuario o contraseña incorrectos")
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)