import streamlit as st
from streamlit_ace import st_ace
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import altair as alt
from vega_datasets import data
import pydeck as pdk


def file_to_code(code_file):
    if code_file:
        code = code_file.read().decode('utf-8')
        return code


def right_codeblock(code=" "):
    history = st.session_state.get('history', [])
    THEMES = [
        "clouds",
        "clouds_midnight",
        "cobalt",
        "xcode",
    ]
    KEYBINDINGS = ["emacs", "sublime", "vim", "vscode"]

    editor, app, hist = st.tabs(["Editor", "App", "History"])

    with editor:
        code = st_ace(value=code,
                      placeholder="st.header('Hello world!')",
                      theme=st.sidebar.selectbox("Theme", options=THEMES),
                      keybinding=st.sidebar.selectbox(
                          "Keybinding mode", options=KEYBINDINGS),
                      show_gutter=True
                      )
    with app:
        try:
            if code != " ":
                exec(code)
            if code not in history and code != " ":
                history.append(code)
                if len(history) > 5:
                    history = history[-5:]
        except Exception as e:
            st.error(f"Error: {str(e)}")

    with hist:
        for idx, hist_code in enumerate(history[::-1]):
            if hist_code != " ":
                st.code(hist_code, language="python")
            if hist_code != " ":
                st.download_button("Save code", data=hist_code, file_name=f"code{idx}.py", use_container_width=True)

        st.session_state['history'] = history
