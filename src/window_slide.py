import streamlit as st


def slide():
    with st.sidebar:
        OPEN_AI = st.text_input("Enter your API key", type="password")
        bt = st.button("Save")
        if bt:
            if "API_KEY" in st.session_state:
                if st.session_state["API_KEY"] != OPEN_AI:
                    st.session_state["API_KEY"] = OPEN_AI
            else:
                st.session_state["API_KEY"] = OPEN_AI

