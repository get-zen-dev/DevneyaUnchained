import streamlit as st
from src.backend import generate_prompt, connection, deno, edit_prompt
from src.codefile import file_to_code


def buttons_left():
    content = st.text_input(label="Write your code request")
    bt = st.button("Send")
    if bt:
        prompt = generate_prompt()
        response = connection(prompt, content)
        return response

def uploader():
    file = st.file_uploader(label="", type="js")
    if file:
        code = file_to_code(file) if file is not None else ""
        return code

def button_edit(code):
    bt = st.button("Edit", use_container_width=True)
    if bt:
        edit = edit_prompt()
        response = connection(edit, code)
        return response


def buttons_right(content):
    bt = st.button("Run", use_container_width=True)
    if bt:
        return deno(content)

def radio_buttons():
    bt = st.radio("",
                          ("Write", "Edit"),
                          horizontal=True
                          )
    return bt
