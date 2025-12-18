"""
QUESTION:
Write a function `convert_dict` that takes a nested dictionary as input and returns a list of tuples containing the keys and their corresponding value data types. The function should recursively convert the values of inner dictionaries and lists, handling data types such as strings, integers, floats, booleans, and None. If a list value contains dictionaries, the function should recursively convert the dictionaries. If a list value contains other types, the function should convert the types. The input dictionary values are strings, except for None values which are null. The function should handle empty lists.
"""

from typing import List, Tuple, Any, Union


def convert_dict(dictionary: dict) -> List[Tuple[str, Any]]:
    result = []
    for key, value in dictionary.items():
        if isinstance(value, dict):
            result.append((key, convert_dict(value)))
        elif isinstance(value, list):
            if len(value) > 0:
                if isinstance(value[0], dict):
                    result.append((key, [convert_dict(v) for v in value]))
                else:
                    result.append((key, [type(v) if v is not None else type(None) for v in value]))
            else:
                result.append((key, value))
        else:
            result.append((key, type(value)))
    return result