"""
QUESTION:
Create two functions, `encode_cyclic(s: str)` and `decode_cyclic(s: str)`, that implement a cyclic encoding and decoding of input strings. The encoding function should shift each character in the string by a value from the cycle [1, 2, 3], wrapping around to the start of the cycle when necessary. The decoding function should reverse this process, shifting each character by the corresponding value in the cycle. Both functions must handle alphabetic characters, numeric values, punctuation, and whitespace, using their corresponding ASCII values.
"""

def encode_cyclic(s: str):
    """
    Currently returns encoded string through a series of three characters cycling, inclusive of numerics and punctuation marks.
    """
    cycle = [1, 2, 3]
    encoded = ''
    for i, char in enumerate(s):
        shift = cycle[i % len(cycle)]
        encoded += chr((ord(char) + shift - 32) % 95 + 32)
    return encoded


def decode_cyclic(s: str):
    """
    Returns decoded string unraveled from encode_cyclic function, dealing with special characters, numerical values, grammatical punctuation and whitespace.
    """
    cycle = [1, 2, 3]
    decoded = ''
    for i, char in enumerate(s):
        shift = cycle[i % len(cycle)]
        decoded += chr((ord(char) - shift - 32) % 95 + 32)
    return decoded