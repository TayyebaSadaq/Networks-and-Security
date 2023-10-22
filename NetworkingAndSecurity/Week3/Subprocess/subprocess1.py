import subprocess

res = subprocess.run("echo Hello", shell=True)

print("------------------")

# print(dir(res)) # show all the attributes and methods of the object

print(*dir(res), sep = "\n") # show all the attributes and methods of the object in a list format (one per line)

