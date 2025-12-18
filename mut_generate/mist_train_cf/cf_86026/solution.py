"""
QUESTION:
Create a function `char_dict(s: str)` that generates a dictionary from a given string `s` where the keys are unique characters and the values are lists containing the ASCII value of the character and a list of ASCII values of the characters in its binary representation. The function should have a time complexity no worse than O(n log n).
"""

def char_dict(s: str) -> dict:
    unique_chars = set(s)
    return {char: [ord(char), [ord(bit) for bit in format(ord(char),'b')]] for char in unique_chars}