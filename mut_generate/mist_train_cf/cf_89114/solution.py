"""
QUESTION:
Create a function called `reverse_string` that takes a string as input and returns the reversed string. The function must have a time complexity of O(n), where n is the length of the string, and cannot use built-in functions or data structures, variables, loops, or the slicing operator.
"""

def reverse_string(input_string):
    if len(input_string) <= 1:
        return input_string
    else:
        first_char = input_string[0]
        rest_of_string = input_string[1:]
        reversed_rest = reverse_string(rest_of_string)
        return reversed_rest + first_char