"""
QUESTION:
Create a function called "string_operations" that takes a string and a boolean as parameters. Replace all occurrences of 'old' with 'new' in the string and remove any trailing whitespace characters. Return the modified string. Note that the boolean parameter "capitalize" does not need to be utilized in the function.
"""

def string_operations(string, capitalize):
    return string.replace('old', 'new').rstrip()