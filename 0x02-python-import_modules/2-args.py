#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argLen = len(sys.argv)
    num_arguments = len(sys.argv) - 1

    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument.")
    else:
        print("{} arguments.".format(num_arguments))

    for i in range(1, argLen):
        print("{} : {}".format(i + 1, sys.argv[i + 1]))
