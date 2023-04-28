import os
import subprocess


def deno(filename):
    cwd = os.getcwd()
    file_path = os.path.join(cwd, filename)
    cmd = ["deno", "run", file_path]
    process = subprocess.run(cmd, capture_output=True, text=True)
    if process.returncode == 0:
        print(process.stdout)
    else:
        print(f"Error running Deno:\n{process.stderr}")

