"""
QUESTION:
Write a Python function `extract_nested_data(json_data: List[str]) -> List[Tuple[str, Union[int, bool, str]]]` that takes a list of JSON strings as input and returns a list of tuples. Each tuple should contain a field name and its corresponding value based on the following criteria:

1. If a field is a top-level key and its value is a boolean or an integer, include it in the output.
2. If a field is nested within the "n" key and its value is a list of strings, include each string in the output with 's' as the field name.

Assume that the input JSON strings are well-formed and do not contain any nested objects deeper than one level.
"""

from typing import List, Tuple, Union
import json

def extract_nested_data(json_data: List[str]) -> List[Tuple[str, Union[int, bool, str]]]:
    result = []
    for data in json_data:
        json_obj = json.loads(data)
        for key, value in json_obj.items():
            if isinstance(value, (bool, int)):
                result.append((key, value))
            elif key == 'n' and isinstance(value, dict):
                for nested_key, nested_value in value.items():
                    if isinstance(nested_value, list) and all(isinstance(item, str) for item in nested_value):
                        for item in nested_value:
                            result.append(('s', item))
    return result