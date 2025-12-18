"""
QUESTION:
Write a function `find_x` that takes a string `text` of length n (where n can be up to 10^5 characters) as input and returns the positions of all occurrences of the character 'x'. If 'x' is not found in the string, the function should return a message stating that 'x' does not exist in the string.
"""

def find_x(text):
    positions = [i for i, ch in enumerate(text) if ch == 'x']
    if positions:
        return positions
    else:
        return "'x' does not exist in the string."