import subprocess

res = subprocess.run(
    "./args1.py apples oranges \"banana split\"",  # command to run
    shell=True, # run the command in a shell
    capture_output = True, # capture the output
    text = True, # convert the output to text
    )

print (res.stdout, end="") # print the output