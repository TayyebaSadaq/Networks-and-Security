import os

# relative to terminal
print(os.getcwd()) # print the current working directory

# relative path to this file
print(__file__)

# absolute path
print(os.path.abspath(__file__))

# absolute path to parent dir
print(os.path.dirname(os.path.abspath(__file__)))