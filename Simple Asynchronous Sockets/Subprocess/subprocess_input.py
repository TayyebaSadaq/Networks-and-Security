import subprocess
import os

# absolute path to parent dir
file_dir = os.path.dirname(os.path.abspath(__file__))


res = subprocess.run(
    f"{file_dir}/input1.py", # program to run
    shell = True, # run in the shell
    input = "apples\noranges\nbanana split\n", # input to the program
    capture_output=True,
    text=True # return stdout as text
)

print(res.stdout, end ="")
print(res.returncode)