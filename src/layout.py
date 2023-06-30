import streamlit as st
from src.buttons import buttons_left
from src.codefile import right_codeblock,commit_deploy



def layout():
    st.markdown("<h1 style='text-align: center; color: black;'>Devneya</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<h2 style='text-align: center; color: dark;'>Write your app request?</h2>", unsafe_allow_html=True)

        result = buttons_left()

        if result is not None:
            content, req = result

            if 'content' not in st.session_state:
                st.session_state['content'] = content
                st.session_state['req'] = req
            elif st.session_state['content'] != content and content is not None:
                st.session_state['content'] = content
                st.session_state['req'] = req
            commit_deploy()
    with col2:
        st.markdown("<h2 style='text-align: center; color: dark;'></h2>", unsafe_allow_html=True)
        if 'content' in st.session_state:
            if st.session_state['content'] is not None:
                code = st.session_state['content']
                lib = st.session_state['req']
                right_codeblock(lib, code)
            else:
                right_codeblock()
