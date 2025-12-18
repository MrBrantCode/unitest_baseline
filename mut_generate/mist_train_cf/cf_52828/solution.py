"""
QUESTION:
Create a function named `my_function` that accepts a single parameter and checks if the input is of the string data type. If the input is a string, return "Input is of string data type", otherwise return "Input is not of string data type".
"""

def entrance(input_string):
    if isinstance(input_string, str):
        return "Input is of string data type"
    else:
        return "Input is not of string data type"