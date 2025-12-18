"""
QUESTION:
Implement a function `find_x` that takes a string as input and returns the index at which the character 'x' is found. If 'x' is not found in the string, return a message indicating that 'x' was not found. You must use a while loop to iterate through the characters in the string.
"""

def find_x(s):
    index = 0
    while index < len(s):
        if s[index] == 'x':
            return index
        index += 1
    return "Letter 'x' not found in the string."