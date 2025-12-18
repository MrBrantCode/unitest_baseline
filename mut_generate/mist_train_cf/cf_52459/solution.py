"""
QUESTION:
Create a function `calculate_utf8_bytes` that takes a string as input and returns the number of UTF-8 bytes needed to encode the string. The function should handle strings containing both ASCII and non-ASCII characters, and it should be efficient in terms of space complexity. Note that the function does not need to perform the actual encoding, but rather calculate the number of bytes required based on the characters in the string.
"""

def calculate_utf8_bytes(input_string):
    """
    Calculate the number of UTF-8 bytes needed to encode the input string.

    Args:
        input_string (str): The input string to calculate UTF-8 bytes for.

    Returns:
        int: The number of UTF-8 bytes needed to encode the input string.
    """
    utf8_bytes = 0
    for char in input_string:
        if ord(char) < 128:
            utf8_bytes += 1  # 1 byte for ASCII characters
        elif ord(char) < 2048:
            utf8_bytes += 2  # 2 bytes for characters in the range of 128-2047
        elif ord(char) < 65536:
            utf8_bytes += 3  # 3 bytes for characters in the range of 2048-65535
        else:
            utf8_bytes += 4  # 4 bytes for characters in the range of 65536-1114111
    return utf8_bytes