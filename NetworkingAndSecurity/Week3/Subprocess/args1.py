import sys

args = sys.argv[1:]

if "-h" in args or "--help" in args: # if the user wants help
    print("Progress to print args.") # print the help text
    print("Options")
    print("-h or --help: print this help text")
    exit(0)

for arg in args:
    print(arg)