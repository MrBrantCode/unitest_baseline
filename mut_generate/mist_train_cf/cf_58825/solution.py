"""
QUESTION:
Write a function `first_non_space_char(s)` that takes a string `s` as input and returns a tuple. The tuple should contain the index of the first non-space character in the string, and a string indicating whether this character is a digit ("Digit") or an alphabet ("Alphabet"). If the first non-space character is neither a digit nor an alphabet, the function should return (-1, -1). If the string contains only spaces, the function should also return (-1, -1).
"""

def first_non_space_char(s):
    for i, c in enumerate(s):
        if not c.isspace():
            if c.isdigit():
                return i, "Digit"
            elif c.isalpha():
                return i, "Alphabet"
            else:
                return -1, -1
    return -1, -1