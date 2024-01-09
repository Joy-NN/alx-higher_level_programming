#!/usr/bin/python3
if __name__ == "__main__":
    import sys

def add_arguments():
    arguments = sys.argv[1:]

    try:
        result = sum(int(arg) for arg in arguments)

        print(result)
    except ValueError as exception:
        print(f"Error: {exception}")

        add_arguments()

