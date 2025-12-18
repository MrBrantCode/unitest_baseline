"""
QUESTION:
Write a function `encode_byte_sequence(output)` that takes a string `output` and returns its corresponding byte sequence in UTF-8 format, where each byte is in the range of 0 to 255 and is in big-endian format. The function should iterate over each character in the string, convert it to its Unicode code point, and then encode it in UTF-8 format.
"""

def encode_byte_sequence(output):
    byte_sequence = []
    for char in output:
        byte_sequence.extend(char.encode('utf-8'))
    return byte_sequence