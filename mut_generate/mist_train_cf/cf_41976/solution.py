"""
QUESTION:
Create a function `hex_to_ascii` that takes a dictionary `input_dict` as input, where each key is an uppercase letter and its corresponding value is a hexadecimal number representing its ASCII value. The function should return a new dictionary where each key is the same uppercase letter and its value is the corresponding ASCII value. The input dictionary will only contain 1 to 26 key-value pairs, with hexadecimal values in the range of 0x20 to 0x7E, representing printable ASCII characters.
"""

def hex_to_ascii(input_dict: dict) -> dict:
    return {key: int(value, 16) for key, value in input_dict.items()}