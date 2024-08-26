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
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        background-color: #008fc4;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown('<p class="big-font">HelPharma</p>', unsafe_allow_html=True)

        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit_button = st.form_submit_button("Login")

        if submit_button:
            if username in USERS and USERS[username] == password:
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.rerun()
            else:
                st.error("Username or password is incorrect")

    st.markdown('<div style="margin-top: 50px;"></div>', unsafe_allow_html=True)