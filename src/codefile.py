import streamlit as st

def file_to_code(code_file):
    if code_file:
        code = code_file.read().decode('utf-8')
        return code

def right_codeblock(code):
    code = st.code(code)

