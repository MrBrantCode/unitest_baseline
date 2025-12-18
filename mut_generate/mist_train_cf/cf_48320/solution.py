"""
QUESTION:
Design a function named `upper_string_process` that takes a string as input and returns a new string containing only the uppercase alphabetic characters from the original string.
"""

def upper_string_process(s):
    return ''.join([char for char in s if char.isupper()])