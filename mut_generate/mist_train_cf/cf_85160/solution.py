"""
QUESTION:
Write a function named `char_positions` that takes two parameters: `text` and `chars`, both of which are strings. The function should return a dictionary where each character in `chars` is a key and its corresponding value is a list of indices where the character appears in `text`. The function should be able to handle multiple characters in `chars`.
"""

def char_positions(text, chars):
    result = {}

    for char in chars:
        result[char] = [i for i, letter in enumerate(text) if letter == char]

    return result