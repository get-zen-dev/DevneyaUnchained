def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


def save_output(response, filename):
    with open(filename, "w") as f:
        f.write(response)
