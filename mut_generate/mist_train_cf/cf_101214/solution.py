"""
QUESTION:
Write a function named extract_coordinates that takes a binary string as input. The function should extract the hemisphere, degrees, minutes, seconds, and another hemisphere from the string, considering the format may vary and have multiple non-contiguous segments. Each segment in the string is represented by a binary value. The function should return the extracted values in a readable format, with hemispheres represented as 'N', 'S', 'E', or 'W' and degrees, minutes, and seconds as integers.
"""

import re

def extract_coordinates(binary_string):
    """
    Extract hemisphere, degrees, minutes, seconds, and another hemisphere from a binary string.

    Args:
        binary_string (str): A binary string containing the coordinates.

    Returns:
        tuple: A tuple containing the extracted values in the following order:
            hemisphere1 (str), degrees (int), minutes (int), seconds (int), hemisphere2 (str)
    """
    pattern = r'(0{32}|1{32})(0{8}|1{8})(0{8}|1{8})(0{8}|1{8})(0{32}|1{32})'
    matches = re.findall(pattern, binary_string)

    if matches:
        hemisphere1, degrees, minutes, seconds, hemisphere2 = matches[0]
        hemisphere1 = 'N' if hemisphere1 == '0'*32 else 'S'
        hemisphere2 = 'E' if hemisphere2 == '0'*32 else 'W'
        degrees = int(degrees, 2)
        minutes = int(minutes, 2)
        seconds = int(seconds, 2)
        
        return hemisphere1, degrees, minutes, seconds, hemisphere2
    else:
        return None