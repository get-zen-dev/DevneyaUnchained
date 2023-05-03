import argparse
import re


def reading_prompt():
    prompt = input("Enter your request:\n")
    return prompt


def save_output(response, filename):
    with open(filename, "w") as f:
        f.write(response)


def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


def specify_lines():
    lines = input("Specify the lines for correction: ").strip()
    lines_list = []
    for line in lines.split():
        if "-" in line:
            start, end = map(int, line.split("-"))
            lines_list += [str(num) for num in range(start, end + 1)]
        else:
            lines_list.append(line.strip())
    return lines_list


def parse_code_blocks(text):
    pattern = '(\d)``` javascript\n([\s\S]*?)\n```'

    data = {}
    for match in re.finditer(pattern, text):
        line_number = match.group(1)
        code = match.group(2)
        data[int(line_number)] = code

    return data


def replace_lines_in_file(lines, filename):
    content = read_file(filename)
    content_lines = content.split('\n')

    for line_number, new_line in lines.items():
        content_lines[int(line_number) - 1] = new_line

    new_file_content = '\n'.join(content_lines)
    # print(new_file_content)
    save_output(new_file_content, filename)


def get_args():
    parser = argparse.ArgumentParser(description="The program receives the coding request and gives working solution")
    parser.add_argument("--save", help="saves solution to output file", action="store_true")
    parser.add_argument("--run", help="sends code to Deno runtime", action="store_true")
    parser.add_argument("--edit", help="edit file by specifying the file path", nargs=1, metavar="filepath")
    args = parser.parse_args()
    return args
