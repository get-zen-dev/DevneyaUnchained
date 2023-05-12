import streamlit as st
from src.buttons import buttons_left,buttons_right,button_edit
from src.codefile import file_to_code




def layout():
    st.markdown("<h1 style='text-align: center; color: black;'>Devneya</h1>", unsafe_allow_html=True)
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("<h2 style='text-align: center; color: dark;'>Write or Edit?</h2>", unsafe_allow_html=True)
        # st.subheader("Write or Edit?")
        option = st.radio("",
                          ("Write", "Edit"),
                          horizontal=True
                          )

        if option == "Write":
            content = buttons_left()
        if option == "Edit":
            code = st.file_uploader(label="", type="js")
            content = file_to_code(code) if code is not None else ""
            # content = button_edit(code.name,content)

    if 'content' not in st.session_state:
        st.session_state['content'] = content
    elif st.session_state['content'] != content and content is not None:
        st.session_state['content'] = content


    with col2:
        st.markdown("<h2 style='text-align: center; color: dark;'>Code</h2>", unsafe_allow_html=True)
        # st.subheader("Code")
        ans = st.code(body=st.session_state['content'], language="javascript", line_numbers=True)
        if option == "Write":
            buttons_right(None,option,st.session_state['content'])
        elif option == "Edit":
            try:
                buttons_right(code.name, option, None)
            except AttributeError:
                buttons_right(None, option, None)
        else:
            try:
                buttons_right(code.name, option, None)
            except AttributeError:
                buttons_right(None, option, None)




