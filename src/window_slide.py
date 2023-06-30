import streamlit as st
from src.connection import git_connection
from src.auth import get_login_str, parse_tokens
from src.buttons import git_button,openai_button


def slide():
    with st.sidebar:
        st.markdown(get_login_str(), unsafe_allow_html=True)
        parse_tokens()
        if "GIT_KEY" in st.session_state:
            access_token = st.session_state["GIT_KEY"]
            user = git_connection(access_token)
            if 'user' not in st.session_state:
                st.session_state['user'] = user
            st.success(f"Welcome {user.name}")
            git_button()
            openai_button()

