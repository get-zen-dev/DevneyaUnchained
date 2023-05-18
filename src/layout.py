import streamlit as st
from src.buttons import buttons_left, buttons_right, radio_buttons, uploader
from src.codefile import right_codeblock


def layout():
    st.markdown("<h1 style='text-align: center; color: black;'>Devneya</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h2 style='text-align: center; color: dark;'>Write or Edit?</h2>", unsafe_allow_html=True)
        option = radio_buttons()
        if option == "Write":
            content = buttons_left()
        elif option == "Edit":
            content = uploader()
    if 'content' not in st.session_state:
        st.session_state['content'] = content
    elif st.session_state['content'] != content and content is not None:
        st.session_state['content'] = content
    with col2:
        st.markdown("<h2 style='text-align: center; color: dark;'>Code</h2>", unsafe_allow_html=True)
        if 'content' in st.session_state:
            right_codeblock(st.session_state['content'])
            output = buttons_right(st.session_state['content'])
            st.code(output)
