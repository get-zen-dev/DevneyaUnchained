import streamlit as st
from src.buttons import buttons_left, radio_buttons, uploader, button_edit
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
            if st.session_state['content'] is not None:
                content = button_edit(content)

    if 'content' not in st.session_state:
        st.session_state['content'] = content
    elif st.session_state['content'] != content and content is not None:
        st.session_state['content'] = content
    with col2:
        st.markdown("<h2 style='text-align: center; color: dark;'>Code</h2>", unsafe_allow_html=True)
        if 'content' in st.session_state:
            if st.session_state['content'] is not None:
                code = st.session_state['content']
                right_codeblock(code)
            else:
                st.code("Enter your API KEY to start")
