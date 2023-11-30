#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argLen = len(sys.argv)
    num_arguments = len(sys.argv) - 1

    if argLen == 1:
        print("{} arguments.".format(num_arguments))
    elif argLen == 2:
        print("{} arguments.".format(num_arguments))
    else:
        print("{} arguments.".format(num_arguments))

    for i in range(1, argLen):
        print("{} : {}".format(i, sys.argv[i]))
