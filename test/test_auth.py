import unittest
import src.auth
from httpx_oauth.clients.github import GitHubOAuth2
import asyncio
from unittest.mock import MagicMock, patch
import streamlit as st


class MyTestCase(unittest.TestCase):

    def test_get_authorization_url(self):
        async def mock_get_authorization_url(client, redirect_uri):
            return 'test_authorization_url'

        client = GitHubOAuth2('test_client_id', 'test_client_secret')
        with patch('httpx_oauth.clients.github.GitHubOAuth2.get_authorization_url',
                   new=MagicMock(side_effect=mock_get_authorization_url)):
            loop = asyncio.get_event_loop()
            authorization_url = loop.run_until_complete(src.auth.get_authorization_url(client, 'test_redirect_uri'))
            self.assertEqual(authorization_url, 'test_authorization_url')

    def test_get_access_token(self):
        async def mock_get_access_token(client, redirect_uri, code):
            return {'access_token': 'test_token'}

        client = GitHubOAuth2('test_client_id', 'test_client_secret')
        with patch('httpx_oauth.clients.github.GitHubOAuth2.get_access_token',
                   new=MagicMock(side_effect=mock_get_access_token)):
            loop = asyncio.get_event_loop()
            token = loop.run_until_complete(src.auth.get_access_token(client, 'test_redirect_uri', 'test_code'))
            self.assertEqual(token, {'access_token': 'test_token'})

    def test_get_login_str(self):
        authorization_url = 'test_authorization_url'

        with patch('streamlit.experimental_get_query_params', return_value={'code': 'test_code'}), \
             patch('streamlit.button', return_value=True):
            client = GitHubOAuth2('test_client_id', 'test_client_secret')
            with patch('httpx_oauth.clients.github.GitHubOAuth2.get_authorization_url',
                       new=MagicMock(return_value=authorization_url)):
                login_str = src.auth.get_login_str()
                expected_html = f'<a href="{authorization_url}" target="_self"><button>Authorise</button></a>'
                self.assertEqual(login_str, expected_html)

    def test_parse_tokens(self):
        with patch('streamlit.experimental_get_query_params', return_value={'code': 'test_code'}):
            client = GitHubOAuth2('test_client_id', 'test_client_secret')
            with patch('httpx_oauth.clients.github.GitHubOAuth2.get_access_token',
                       new=MagicMock(return_value={'access_token': 'test_token'})):
                with patch.dict(st.session_state, {}, clear=True):
                    src.auth.parse_tokens()
                    self.assertEqual(st.session_state["code"], 'test_code')
                    self.assertEqual(st.session_state["GIT_KEY"], 'test_token')


if __name__ == '__main__':
    unittest.main()
