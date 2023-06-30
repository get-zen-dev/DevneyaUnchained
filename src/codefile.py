import streamlit as st


def create_files(repo, app_name, selected_code, text):
    try:
        repo.create_file(f"{app_name}.py", "Devneya", selected_code, branch="main")
        repo.create_file("requirements.txt", "Devneya", text, branch="main")
        st.success("Commit is successful. Visit [here](https://share.streamlit.io/deploy) for deployment.")
    except Exception as e:
        st.error(f"An error occurred while creating files: {str(e)}")


def update_files(repo, app_name, selected_code, text):
    try:
        branch = "main"
        file_path_1 = f"{app_name}.py"
        file_path_2 = "requirements.txt"

        sha_1 = repo.get_contents(file_path_1, ref=branch).sha
        sha_2 = repo.get_contents(file_path_2, ref=branch).sha

        repo.update_file(file_path_1, "Updating file", selected_code, sha_1, branch=branch)
        repo.update_file(file_path_2, "Updating file", text, sha_2, branch=branch)

        st.success("Commit was successful.")
    except Exception as e:
        st.error(f"An error occurred while updating files: {str(e)}")


def commit_deploy():
    user = st.session_state['user']
    selected_code = st.session_state["content"]
    text = st.session_state['req']
    update_files(st.session_state['repo'], "streamlit_app", selected_code, text)


def right_codeblock(lib="", code=""):
    prog, app = st.tabs(["Code", "App"])
    with prog:
        if code != "":
            st.code(code)
            # commit_deploy()
    with app:
        website_name = st.text_input("Enter the name of the website:")
        try:
            if website_name.startswith("http://") or website_name.startswith("https://"):
                url = website_name + "/?embed=True"
                st.markdown(f'<embed src="{url}" width="100%" height="600">', unsafe_allow_html=True)
            else:
                None
        except Exception as e:
            st.error(f"Error: {str(e)}")