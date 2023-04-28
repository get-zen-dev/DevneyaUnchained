import os


def create_config_dir():
    config_dir = os.path.expanduser("~/.config/openai")

    if not os.path.exists(config_dir):
        os.makedirs(config_dir)


def create_credentials_file(api_key):
    config_dir = os.path.expanduser("~/.config/openai")
    credentials_file = os.path.join(config_dir, "credentials")

    with open(credentials_file, "w") as f:
        f.write("OPENAI_API_KEY=" + api_key)


def load_credentials():
    config_dir = os.path.expanduser("~/.config/openai")
    credentials_file = os.path.join(config_dir, "credentials")

    with open(credentials_file, "r") as f:
        line: str
        credentials = dict(line.strip().split("=", 1) for line in f)

    return credentials


def prompt_for_api_key():
    api_key = input("Enter your OpenAI API key: ")
    return api_key


def get_api_key():
    create_config_dir()

    try:
        credentials = load_credentials()
    except FileNotFoundError:
        credentials = {}

    if "OPENAI_API_KEY" not in credentials:
        api_key = prompt_for_api_key()
        create_credentials_file(api_key)
    else:
        api_key = credentials["OPENAI_API_KEY"]

    return api_key
