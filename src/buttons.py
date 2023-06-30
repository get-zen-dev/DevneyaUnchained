import streamlit as st
from src.prompt import generate_prompt, lib_prompt
from src.connection import connection


def create_files(repo, app_name, selected_code, text):
    try:
        repo.create_file(f"{app_name}.py", "Devneya", selected_code, branch="main")
        repo.create_file("requirements.txt", "Devneya", text, branch="main")
        st.success("Commit is successful. Visit [here](https://share.streamlit.io/deploy) for deployment.")
    except Exception as e:
        st.error(f"An error occurred while creating files: {str(e)}")


def buttons_left():
    content = st.text_area(label="Write your code request", height=200, key="text_area")

    st.markdown(
        f"""
        <style>
        .square-text-area textarea {{
            width: 200px;
            height: 200px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    bt = st.button("Commit and Deploy", use_container_width=True)
    if bt:
        prompt = generate_prompt()
        response = connection(prompt, content)
        libprompt = lib_prompt()
        req = connection(libprompt, response)
        return response, req


def openai_button():
    open_ai = st.text_input("Enter your API key", type="password")
    bt = st.button("Save")
    if bt:
        if "API_KEY" in st.session_state:
            if st.session_state["API_KEY"] != open_ai:
                st.session_state["API_KEY"] = open_ai
        else:
            st.session_state["API_KEY"] = open_ai


def git_button():
    rep = st.text_input("Enter the name for your project")
    bt = st.button("Create")
    if bt:
        user = st.session_state['user']
        repo_name = rep
        repo = user.create_repo(repo_name)
        if 'repo' not in st.session_state:
            st.session_state['repo'] = repo
        st.success(f"Repository '{repo_name}' created successfully!")
        create_files(repo, "streamlit_app", " ", " ")
