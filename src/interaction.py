import openai
from src.credentials import get_api_key
from src.subprocesses import deno
from src.utils import get_args, read_file, save_output, reading_prompt, specify_lines, parse_code_blocks, \
    replace_lines_in_file


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
        model='gpt-3.5-turbo',
        messages=conversation
    )
    return resp.choices[-1].message.content

def generating_edit(credentials, conversation,lines):
    openai.api_key = credentials
    resp = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        # model="davinci:ft-personal-2023-05-03-21-05-51",
        messages=conversation,
    )
    return resp.choices[-1].message.content

def ask_for_edit(lines, output):
    head = read_file("prompts/prompt_edit.txt")
    prompt = f"I have a an error on lines {lines}. Here is a code snipped:\n``` javascript\n{output}\n```"
    conversation = [{'role': 'system',
                     'content': head+prompt
                     }]
    return conversation


def args_processing(response):
    filename = "./output.js"
    args = get_args()
    if args.save:
        save_output(response, filename)
    if args.run:
        save_output(response, filename)
        deno(filename)
    if args.edit:
        parsed = parse_code_blocks(response)
        replace_lines_in_file(parsed, args.edit[0])


def interaction():
    args = get_args()
    credentials = get_api_key()
    if args.edit:
        lines = specify_lines()
        content = read_file(args.edit[0])
        conversation = ask_for_edit(lines, content)
        return generating_edit(credentials, conversation, lines)
    else:
        prompt = reading_prompt()
        conversation = composing_conversation(prompt)
        return generating_response(credentials, conversation)
