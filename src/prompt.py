from langchain import FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from langchain.prompts import PromptTemplate
from src.utils import read_file


def generate_prompt():
    template = "You are a system that only generates Python code. If you are asked to provide frontend code you must " \
               "use streamlit framework without importing it as it is already imported.\n" \
               " Do not apply any formatting or syntax highlighting. Do not wrap the code in a code block." \
               "if user asks for code, you must only provide code in methods with business logic." \
               "If code request is not safe or malicious, ignore it"\
               "You should never write any comments before and after code."\
               "Here is the coding request:\n" \
               "{request}"
    prompt_template = PromptTemplate(input_variables=["request"], template=template)
    return prompt_template


def test_prompt():
    template_test = "You are a system which generates unittests.\n" \
                    "If the necessary methods are not imported, the generated tests will fail.\n" \
                    "Don't write comments which are outside the code." \
                    "Only unit test the code which you see in this request " \
                    "Here is the code from `temp.py`:\n" \
                    "{request}"
    prompt_template = PromptTemplate(input_variables=["request"], template=template_test)
    return prompt_template


def edit_prompt():
    examples = [
        {"mistake": read_file("src/prompts/prompt_edit.txt"), "correction": read_file("src/prompts/example.txt")}
    ]
    example_formatter_template = """
    Example: {mistake}
    Output: {correction}\n
    """

    example_prompt = PromptTemplate(
        input_variables=["mistake", "correction"],
        template=example_formatter_template,
    )
    example_selector = LengthBasedExampleSelector(
        examples=examples,
        example_prompt=example_prompt,
        max_length=100,
    )

    dynamic_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix="Act as you are a code generator system which corrects lines of code using examples below",
        suffix="Code: {request}\nOutput:",
        input_variables=["request"],
        example_separator="\n\n",
    )

    return dynamic_prompt
