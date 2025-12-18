"""
QUESTION:
Write a function named `strip_and_reverse_string` that takes a string as input, removes all white spaces from the string (excluding leading and trailing white spaces), reverses the resulting string, and returns the result. The input string can contain special characters and numbers.
"""

def strip_and_reverse_string(my_string):
    return my_string.strip().replace(" ", "")[::-1]