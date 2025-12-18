"""
QUESTION:
Write a function called "string_operations" that takes in two parameters: a string and a boolean. The function should replace all occurrences of 'old' with 'new' in the input string, remove any whitespace characters from the right end of the string, and return the modified string. Note that the boolean parameter "capitalize" is required but its value does not affect the function's behavior.
"""

def string_operations(string, capitalize):
    return string.replace('old', 'new').rstrip()