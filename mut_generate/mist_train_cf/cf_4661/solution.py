"""
QUESTION:
Create a function called `encode_byte_sequence` that takes a string of Unicode characters as input and returns the corresponding byte sequence in UTF-8 format. The byte sequence should consist of integers in the range of 0 to 255 and be in big-endian format. The function should encode each character in the input string to its corresponding Unicode code point and then encode it in UTF-8 format.
"""

def encode_byte_sequence(output):
    byte_sequence = []
    for char in output:
        byte_sequence.extend(char.encode('utf-8'))
    return byte_sequence