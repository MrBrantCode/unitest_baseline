"""
QUESTION:
Write a function `check_input_type(input)` that takes one parameter of any data type and returns a string describing the type of the input. The function should handle potential errors using a try-except block and print an error message if an error occurs. Do not use any built-in Python functions or libraries for type checking, and ensure the function can handle input values of different data types such as integers, strings, lists, and others.
"""

def check_input_type(input):
    try:
        if isinstance(input, int):
            return "The input is an integer"
        elif isinstance(input, str):
            return "The input is a string"
        elif isinstance(input, list):
            return "The input is a list"
        else:
            return "The input is of an unknown type"
    except Exception as e:
        print("An error occurred:", str(e))