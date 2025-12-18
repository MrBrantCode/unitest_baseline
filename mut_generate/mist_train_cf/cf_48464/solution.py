"""
QUESTION:
Write a function named `greet` that takes an input `names` and prints a greeting for each name. The function should accept both individual strings and lists of strings as input. If the input is not a string or a list of strings, the function should print a custom error message. The function should handle an unspecified number of names.
"""

def greet(names):
    if isinstance(names, str):
        print(f"Hello {names}")
    elif isinstance(names, list):
        for name in names:
            if not isinstance(name, str):
                print("Invalid input. Please input a string or a list of strings.")
                return
            print(f"Hello {name}")
    else:
       print("Invalid input. Please input a string or a list of strings.")