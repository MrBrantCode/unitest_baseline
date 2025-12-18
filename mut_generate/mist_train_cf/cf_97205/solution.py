"""
QUESTION:
Write a function called "string_operations" that takes in two parameters: a string and a boolean. The function should replace all occurrences of the word 'old' with the word 'new' in the input string in a case-insensitive manner if the boolean parameter is True, otherwise the replacement should be case-sensitive. The function should also remove any whitespace characters from both the left and right ends of the string. The function should return the modified string.
"""

def string_operations(string, case_sensitive):
    if case_sensitive:
        return string.strip().replace('old', 'new')
    else:
        return string.strip().lower().replace('old', 'new')