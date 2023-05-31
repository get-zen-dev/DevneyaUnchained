import streamlit as st


def slide():
    with st.sidebar:
        OPEN_AI = st.text_input("Enter your API key", type="password")
        bt = st.button("Save")
        if bt and "API_KEY" not in st.session_state:
            st.session_state["API_KEY"] = OPEN_AI

