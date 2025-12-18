"""
QUESTION:
Create a function `reverse_string` that takes a string `s` as input and returns the characters of the string in reverse order without using any built-in functions to reverse the string or aid directly in the process. The function should handle edge cases, such as empty strings or single character strings, and be able to process extremely long strings efficiently.
"""

def reverse_string(s):
    result = ''
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result