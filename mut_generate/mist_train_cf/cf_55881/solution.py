"""
QUESTION:
Create a function named `array_to_string` that transforms an array of integers, each ranging from 0 to 255, into a string representation. The integers should be converted to their corresponding ASCII characters. Note that some numbers may not be mapped to printable ASCII characters.
"""

def array_to_string(array):
    return ''.join(chr(i) for i in array)