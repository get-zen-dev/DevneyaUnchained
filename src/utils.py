import argparse
from src.subprocesses import deno


def reading_prompt():
    prompt = input("Enter your request:\n")
    return prompt


def save_output(response, filename):
    with open(filename, "w") as f:
        f.write(response)


def get_args():
    parser = argparse.ArgumentParser(description="The program receives the coding request and gives working solution")
    parser.add_argument("--save", help="saves solution to output file", action="store_true")
    parser.add_argument("--run", help="sends code to Deno runtime", action="store_true")
    args = parser.parse_args()
    return args


def args_processing(response):
    filename = "./output.js"
    args = get_args()
    if args.save:
        save_output(response, filename)
    if args.run:
        save_output(response, filename)
        deno(filename)
