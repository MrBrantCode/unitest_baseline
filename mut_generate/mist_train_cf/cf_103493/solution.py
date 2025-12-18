"""
QUESTION:
Write a function `reverse_uppercase_string` that takes a string as input. The input string must contain only alphabetical characters and have a length of at least 5. The function should return the input string in uppercase and in reverse order.
"""

def reverse_uppercase_string(s):
    if len(s) >= 5 and s.isalpha():
        return s[::-1].upper()
    else:
        return "Input string should contain only alphabetical characters and have a length of at least 5."