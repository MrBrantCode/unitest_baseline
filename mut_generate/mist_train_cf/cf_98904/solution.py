"""
QUESTION:
Write a function called `extract_coordinates` that takes a binary string as input and returns the extracted hemisphere, degrees, minutes, seconds, and hemisphere. The input string may have multiple non-contiguous segments with variations in formatting, including missing or extraneous characters. Each segment is 8 or 32 bits long and represents either a hemisphere (32 bits) or degrees, minutes, or seconds (8 bits). The hemisphere is represented by either all zeros or all ones, with all zeros corresponding to 'N' or 'E' and all ones corresponding to 'S' or 'W'.
"""

import re

def extract_coordinates(binary_string):
    pattern = r'(0{32}|1{32})(0{8}|1{8})(0{8}|1{8})(0{8}|1{8})(0{32}|1{32})'
    matches = re.findall(pattern, binary_string)

    if matches:
        hemisphere1, degrees, minutes, seconds, hemisphere2 = matches[0]
        hemisphere1 = 'N' if hemisphere1 == '0'*32 else 'S'
        hemisphere2 = 'E' if hemisphere2 == '0'*32 else 'W'
        degrees = str(int(degrees, 2))
        minutes = str(int(minutes, 2))
        seconds = str(int(seconds, 2))
        
        return {
            'hemisphere': hemisphere1,
            'degrees': degrees,
            'minutes': minutes,
            'seconds': seconds,
            'hemisphere2': hemisphere2
        }
    else:
        return None