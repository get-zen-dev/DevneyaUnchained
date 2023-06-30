from httpx_oauth.clients.github import GitHubOAuth2
import asyncio
import os
import streamlit as st

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
redirect_uri = os.environ['REDIRECT_URI']


async def get_authorization_url(client: GitHubOAuth2, redirect_uri: str):
    authorization_url = await client.get_authorization_url(redirect_uri, scope=["repo"])
    return authorization_url


async def get_access_token(client: GitHubOAuth2, redirect_uri: str, code: str):
    token = await client.get_access_token(code, redirect_uri)
    return token


def get_login_str():
    client: GitHubOAuth2 = GitHubOAuth2(client_id, client_secret)
    authorization_url = asyncio.run(get_authorization_url(client, redirect_uri))
    button_html = f'<a href="{authorization_url}" target="_self"><button>Authorise</button></a>'

    return button_html


def parse_tokens():
    client: GitHubOAuth2 = GitHubOAuth2(client_id, client_secret)
    try:
        code = st.experimental_get_query_params()['code']
        token = asyncio.run(get_access_token(client, redirect_uri, code))

        if 'access_token' in token:
            st.session_state["GIT_KEY"] = token['access_token']
        else:
            pass
    except KeyError:
        code = None
    st.session_state["code"] = code
