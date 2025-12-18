"""
QUESTION:
Implement a function `test_utf8_query` that takes a list of integers representing bytes and returns `True` if it forms a valid UTF-8 encoding and `False` otherwise. The UTF-8 encoding rules are as follows: 
- A character in UTF-8 can be from 1 to 4 bytes long.
- For a 1-byte character, the first bit is a 0, followed by its Unicode code.
- For an n-byte character, the first n bits are all ones of the form 110... followed by n-1 bytes with the most significant 2 bits being 10.
"""

from typing import List

def test_utf8_query(data: List[int]) -> bool:
    num_bytes = 0
    for byte in data:
        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0