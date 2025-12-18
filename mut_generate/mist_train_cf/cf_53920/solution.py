"""
QUESTION:
Construct a function called `letter_position(s, letter)` that takes a string `s` and a single character `letter` as input. Replace all occurrences of `letter` in `s` with their respective 0-based indices within `s`. Return the modified string.
"""

def letter_position(s, letter):
    return ''.join(str(i) if c == letter else c for i, c in enumerate(s))