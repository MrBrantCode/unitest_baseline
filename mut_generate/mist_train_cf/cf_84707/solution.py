"""
QUESTION:
Given a string of lowercase English alphabets, write a function `char_positions` that returns a dictionary with 'x', 'y', and 'z' as keys. The values should be lists containing the positions of their respective characters in the string. The positions are 0-indexed, meaning the first character is at position 0.
"""

def char_positions(s):
    d = {'x': [], 'y': [], 'z': []}
    for i, char in enumerate(s):
        if char in d:
            d[char].append(i)
    return d