"""
QUESTION:
Create a function called `find_string_length` that calculates the length of a given string without using built-in string length functions or methods. The function should take one parameter, the input string `s`, and return the length of the string. The function should work with any string input, but does not need to handle non-string inputs.
"""

def find_string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count