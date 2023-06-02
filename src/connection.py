from langchain.llms import OpenAI
from langchain import LLMChain
import streamlit as st


def connection(prompt_title, question):
    if "API_KEY" in st.session_state:
        try:
            model = OpenAI(temperature=0, max_tokens=2500, openai_api_key=st.session_state["API_KEY"])
            if question != "":
                title_chain = LLMChain(llm=model, prompt=prompt_title)
                response = title_chain.run(request=question)
                return response
            else:
                title_chain = LLMChain(llm=model, prompt=prompt_title)
                response = title_chain.run(input=question)
                return response
        except Exception as e:
            st.warning("Invalid or incorrect API key. Please check your API key.")
            return None
    else:
        st.warning(
            "Enter your OPENAI API-KEY. Get your OpenAI API key from [here]("
            "https://platform.openai.com/account/api-keys).\n")
        return None
