"""
QUESTION:
Implement a `ParseException` class that inherits from the `Exception` class with an `__init__` method accepting `msg`, `kv_pair`, and optional `args`. Then, implement a `parse_dict` function that takes a dictionary `input_dict` as input, converts keys to uppercase and squares values, and raises `ParseException` if non-numeric values are found. The `ParseException` should contain the error message, key-value pair causing the exception, and any additional arguments. The function should return the resulting dictionary with the transformations applied.
"""

from typing import Dict

class ParseException(Exception):
    def __init__(self, msg: str, kv_pair: Dict, *args: object) -> None:
        super().__init__(*args)
        self.msg = msg
        self.kv_pair = kv_pair

def parse_dict(input_dict: Dict) -> Dict:
    result_dict = {}
    for key, value in input_dict.items():
        if not isinstance(value, (int, float)):
            raise ParseException(f"Non-numeric value found for key '{key}'", {key: value})
        result_dict[key.upper()] = value ** 2
    return result_dict