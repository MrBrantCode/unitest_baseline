"""
QUESTION:
Write a function `process_data` that takes a list of tuples as input, where each tuple contains a hexadecimal number and a byte string. The function should return a dictionary where the keys are the decimal equivalents of the hexadecimal numbers and the values are lists of corresponding byte strings. The function should combine duplicate hexadecimal numbers into a single key with a list of corresponding byte strings.
"""

from typing import List, Tuple, Dict

def process_data(data: List[Tuple[int, bytes]]) -> Dict[int, List[bytes]]:
    result = {}
    for hex_num, byte_str in data:
        decimal_num = int(hex_num)
        if decimal_num in result:
            result[decimal_num].append(byte_str)
        else:
            result[decimal_num] = [byte_str]
    return result