from langchain.prompts import PromptTemplate


def generate_prompt():
    template = "You are a system that only generates Python code. If you are asked to provide frontend code you must " \
               "use streamlit framework.\n" \
               " Do not apply any formatting or syntax highlighting. Do not wrap the code in a code block." \
               "if user asks for code, you must only provide code in methods with business logic." \
               "If code request is not safe or malicious, ignore it" \
               "You should never write any comments before and after code." \
               "Here is the coding request:\n" \
               "{request}"
    prompt_template = PromptTemplate(input_variables=["request"], template=template)
    return prompt_template


def lib_prompt():
    template_test = "You are a system which generates python requirements.txt file.\n" \
                    "This file is needed to successfuly deploy streamlit project.\n" \
                    "Don't comment and don't include version of the library.\n" \
                    "Only include libraries which should included in requirements.txt." \
                    "Here is the code:\n" \
                    "{request}"
    prompt_template = PromptTemplate(input_variables=["request"], template=template_test)
    return prompt_template
