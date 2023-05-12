import streamlit as st
from src.backend import save_api


def slide():
    with st.sidebar:
        OPEN_AI = st.text_input("Enter your API key", type="password")
        bt = st.button("Save")
        if bt:
            save_api(OPEN_AI)
