"""
QUESTION:
Write a function named `capitalize_string` that takes a string as input and returns the string with its first letter capitalized and the remaining characters in lower case. The input string may contain leading or trailing white spaces, be empty, or contain special characters. The function should handle these scenarios correctly.
"""

def capitalize_string(s):
    s = s.strip()
    if s:
        s = s.lower()
        s = s[0].upper() + s[1:]
    return s