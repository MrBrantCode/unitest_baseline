"""
QUESTION:
Write a function `find_positions(text, char)` that takes a string `text` and a character `char` as input and returns a list of positional indices where `char` occurs in `text`.
"""

def find_positions(text, char):
    return [i for i, letter in enumerate(text) if letter == char]