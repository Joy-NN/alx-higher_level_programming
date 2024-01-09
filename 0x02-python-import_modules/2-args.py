#!/usr/bin/python3

import sys
def print_arguments():
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 argument.")
        print(".")
    else:
         print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}.")
         print(".")
         for i, arg in enumerate(sys.argv[1:], start=1):
             print(f"{i}: {arg}")


if __name__ == "__main__":

    sys.argv = ["2-args.py", "I", "love", "that", "I", "am", "African"]
    print_arguments()

