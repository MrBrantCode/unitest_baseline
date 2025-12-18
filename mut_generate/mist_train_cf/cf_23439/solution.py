"""
QUESTION:
Create a function called `hash` that takes a string as input and returns a hash code. The hash code is calculated by summing up the ASCII values of all characters in the string.
"""

def hash(string):
    result = 0
    for char in string:
        result += ord(char)
    return result