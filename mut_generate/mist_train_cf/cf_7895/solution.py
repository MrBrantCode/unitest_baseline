"""
QUESTION:
Write a function `convert_string` that takes a string `s` as input and returns the string with all occurrences of 'c' replaced with 'd'. The function must use a single recursive call and cannot use any loops or conditional statements other than the base case and a single if statement.
"""

def convert_string(s):
    if len(s) == 0:
        return ""
    if s[0] == 'c':
        return 'd' + convert_string(s[1:])
    return s[0] + convert_string(s[1:])