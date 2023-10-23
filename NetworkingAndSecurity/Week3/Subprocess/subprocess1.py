import subprocess

res = subprocess.run(
    "echo Hello", 
    shell=True, # run the command in a shell
    capture_output = True, # capture the output
    text = True, # convert the output to text
    )

print("------------------")

# print(dir(res)) # show all the attributes and methods of the object

print(*dir(res), sep = "\n") # show all the attributes and methods of the object in a list format (one per line)
print("------------------")
print(res.stdout, end = "") # None means no output
print("------------------")
print(res.stderr, end = "") # None means no error
print("------------------") 
print(res.returncode) # 0 means success, 1 means failure