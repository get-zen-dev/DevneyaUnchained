import streamlit as st
from streamlit_metrics import metric, metric_row
from streamlit_ace import st_ace
import numpy as np
import pandas as pd


def file_to_code(code_file):
    if code_file:
        code = code_file.read().decode('utf-8')
        return code


def right_codeblock(code=" "):
    THEMES = [
        "ambiance",
        "chaos",
        "chrome",
        "clouds",
        "clouds_midnight",
        "cobalt",
        "xcode",
    ]
    KEYBINDINGS = ["emacs", "sublime", "vim", "vscode"]

    editor, app = st.tabs(["Editor", "App"])

    with editor:
        code = st_ace(value=code, placeholder="st.header('Hello world!')")
    with app:
        exec(code)
