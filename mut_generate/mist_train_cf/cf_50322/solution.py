"""
QUESTION:
Design a function `add_char(s, p, c)` that takes in three parameters: a string `s`, a position `p`, and a character `c`. The function should insert the character `c` at the specified position `p` in the string `s` and return the resulting string. The position is 0-indexed, meaning the first character in the string is at position 0.
"""

def add_char(s, p, c):
    """
    s is the original string
    p is the position at which to insert the new character
    c is the character to add
    """
    # split the string into two parts
    s1 = s[:p]
    s2 = s[p:]
    
    # add the character to the first part and add the second part
    s = s1 + c + s2
    
    return s