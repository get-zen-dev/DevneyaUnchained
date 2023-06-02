import streamlit as st
from src.prompt import generate_prompt, edit_prompt
from src.connection import connection
from src.codefile import file_to_code


def buttons_left():
    content = st.text_input(label="Write your code request")
    bt = st.button("Send")
    if bt:
        prompt = generate_prompt()
        response = connection(prompt, content)
        return response


def uploader():
    file = st.file_uploader(label="", type="py")
    if file:
        code = file_to_code(file) if file is not None else ""
        return code


def button_edit(code):
    bt = st.button("Edit")
    if bt:
        edit = edit_prompt()
        response = connection(edit, code)
        return response


def radio_buttons():
    bt = st.radio("",
                  ("Write", "Edit"),
                  horizontal=True
                  )
    return bt
