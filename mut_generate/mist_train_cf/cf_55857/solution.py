"""
QUESTION:
Create a function `reverse_string` that takes a single input string as an argument and returns the reversed string using a while loop without any built-in functions or methods. The function should also include input validation to ensure the input is a non-empty string containing only alphabets. If the input is invalid, the function should return "Error: Invalid input".
"""

def reverse_string(input_string):
    if not isinstance(input_string, str) or not input_string.isalpha():
        return "Error: Invalid input"
    reversed_string = ''
    index = len(input_string) - 1
    while index >= 0:
        reversed_string += input_string[index]
        index -= 1
    return reversed_string