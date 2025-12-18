"""
QUESTION:
Implement the function `encode_and_map_data(data: Dict[str, int], encoding_style: str, constants: List[int]) -> List[str]` that takes in the following parameters:
- `data`: A dictionary containing key-value pairs where keys are strings and values are integers.
- `encoding_style`: A string representing the encoding style where 'A' adds a constant, 'M' multiplies by a constant, and 'S' subtracts a constant.
- `constants`: A list of integers corresponding to the constants for each operation in the encoding style.

The function should apply the encoding operations specified by `encoding_style` using the corresponding constants from the `constants` list, then map the encoded data to a list of strings in the format "key:value". 

Assume the length of `data` is between 1 and 10^5, the length of `encoding_style` is between 1 and 10, and the length of `constants` is equal to the length of `encoding_style`.
"""

from typing import Dict, List

def encode_and_map_data(data: Dict[str, int], encoding_style: str, constants: List[int]) -> List[str]:
    encoded_data = data.copy()
    for op, constant in zip(encoding_style, constants):
        if op == 'A':
            encoded_data = {key: value + constant for key, value in encoded_data.items()}
        elif op == 'M':
            encoded_data = {key: value * constant for key, value in encoded_data.items()}
        elif op == 'S':
            encoded_data = {key: value - constant for key, value in encoded_data.items()}
    
    mapped_data = [f"{key}:{value}" for key, value in encoded_data.items()]
    return mapped_data