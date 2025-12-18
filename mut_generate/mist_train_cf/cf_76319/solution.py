"""
QUESTION:
Create a function `reverse_string` that takes an input string and returns a new string that is the reverse of the input string. The function must not use any predefined Python functions or methods for reversing strings, such as `[::-1]` or `reversed()`, and it must handle multibyte Unicode characters correctly.
"""

def reverse_string(input_string):
    return ''.join([input_string[i] for i in range(len(input_string)-1, -1, -1)])