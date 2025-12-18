"""
QUESTION:
Create a function named `find_string_length` that calculates the length of a given string without using any built-in string length functions or methods. The function should take a string `s` as input and return the length of the string as an integer. The function should only work with string inputs.
"""

def find_string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count