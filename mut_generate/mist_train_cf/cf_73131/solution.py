"""
QUESTION:
Write a function named `replace_alternating` that takes two parameters: `string` and `replace_char`, and replaces characters at even indexes in the string with the specified `replace_char`. The function should not use the built-in string `replace` function and should return the modified string.
"""

def replace_alternating(string, replace_char):
    string = list(string)
    for i in range(0, len(string), 2): 
        string[i] = replace_char
    return ''.join(string)