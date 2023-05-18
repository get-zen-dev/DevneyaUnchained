import os
import subprocess
from langchain import FewShotPromptTemplate, LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector


def save_api(OPEN_AI):
    os.environ['OPENAI_API_KEY'] = OPEN_AI


def save_output(response, filename):
    with open(filename, "w") as f:
        f.write(response)


def deno(content):
    cwd = os.getcwd()
    temp_file_path = os.path.join(cwd, "temp.js")
    save_output(content, temp_file_path)
    cmd = ["deno", "run", temp_file_path]
    process = subprocess.run(cmd, capture_output=True, text=True)
    os.remove(temp_file_path)
    if process.returncode == 0:
        return process.stdout
    else:
        return f"Error running Deno:\n{process.stderr}"


def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


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
        prefix="Act as you are a code generator system which corrects lines of code using examples below. You provide only 1 corrected line in a block.",
        suffix="Code: {input}\nOutput:",
        input_variables=["input"],
        example_separator="\n\n",
    )

    return dynamic_prompt


def generate_prompt():
    prompt_title = PromptTemplate(
        input_variables=['request'],
        template='You are a system that only generates code for Deno Runtime. Do not describe or contextualize the '
                 'code. Do not apply any formatting or syntax highlighting. Do not wrap the code in a code block.'
                 '{request}'
    )
    return prompt_title


def connection(prompt_title, question):
    model = OpenAI(temperature=0, max_tokens=2500)
    if question != "":
        title_chain = LLMChain(llm=model, prompt=prompt_title)
        response = title_chain.run(request=question)
        return response
    else:
        title_chain = LLMChain(llm=model, prompt=prompt_title)
        response = title_chain.run(input=question)
        return response

