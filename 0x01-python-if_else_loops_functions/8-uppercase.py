#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
print()
