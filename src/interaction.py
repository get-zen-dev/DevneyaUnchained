import openai
from src.credentials import get_api_key
from src.subprocesses import deno
from src.utils import get_args


def reading_prompt():
    prompt = input("Enter your request:\n")
    return prompt


def save_output(response, filename):
    with open(filename, "w") as f:
        f.write(response)


def composing_conversation(prompt):
    simple = "You are a system that only generates code for Deno Runtime. Do not describe or contextualize the code. " \
             "Do not apply any " \
             "formatting or syntax highlighting. Do not wrap the code in a code block. "

    conversation = [{'role': 'system',
                     'content': simple + prompt
                     }]
    return conversation


def generating_response(credentials, conversation):
    openai.api_key = credentials
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    return resp.choices[-1].message.content


def args_processing(response):
    filename = "./output.js"
    args = get_args()
    if args.save:
        save_output(response, filename)
    if args.run:
        save_output(response, filename)
        deno(filename)


def interaction():
    credentials = get_api_key()
    prompt = reading_prompt()
    conversation = composing_conversation(prompt)
    return generating_response(credentials, conversation)
