"""
QUESTION:
Write a function `swap_chars(string)` that takes a string as input and returns a new string where characters at even and odd indices are swapped. If the string has an odd length, the last character (at an even index) remains unchanged.
"""

def swap_chars(string):
    result = ""
    for i in range(0, len(string), 2):
        if i+1 < len(string):
            result += string[i+1] + string[i]
        else:
            result += string[i]
    return result