from src.layout import layout
import streamlit as st
from src.window_slide import slide


def main():
    st.set_page_config(page_title="Devneya Unchained", layout="wide")
    slide()
    layout()



if __name__ == '__main__':
    main()
