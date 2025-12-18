"""
QUESTION:
Write a function called `print_string_with_lower_asterisks` that takes a string as input and returns the string with all asterisks in lower case. You cannot use built-in string manipulation functions, regular expressions, or loops.
"""

def print_string_with_lower_asterisks(s):
    return s.replace('*', '*').lower() if '*' in s else s