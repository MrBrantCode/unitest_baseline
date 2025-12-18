"""
QUESTION:
Create a function `encode_dict_values` that takes a dictionary as input and returns a new dictionary where all values are encoded to utf-8 strings. The function should handle potentially harmful characters that violate JSON syntax. The output should be suitable for use with `json.dumps()` or `json.dump()` with the `ensure_ascii=False` parameter.
"""

import json

def encode_dict_values(input_dict):
    return {key: str(value).encode('utf-8') for key, value in input_dict.items()}