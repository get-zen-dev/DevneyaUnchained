import streamlit as st
from src.backend import generate_prompt, connection, deno, edit_prompt


def buttons_left():
    content = st.text_input(label="Write your code request")
    bt = st.button("Send")
    if bt:
        prompt = generate_prompt()
        response = connection(prompt, content)
        return response


def button_edit(filename, content):
    bt = st.button("Edit", use_container_width=True)
    if bt:
        edit = edit_prompt()
        response = connection(edit, content)
        # save_output(response,"edit.js")
        # content =
        return response


def buttons_right(filename, option, content):
    bt = st.button("Run", use_container_width=True)
    if bt:
        deno(filename, option, content)
