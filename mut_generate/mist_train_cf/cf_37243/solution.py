"""
QUESTION:
Implement a function `inspect_dict_data` that takes a dictionary `data`, a string `descr`, and an optional integer `level` (default 1) as input. The function should recursively search the nested dictionary for the specified `descr` and return the key associated with it. If the `descr` is not found, the function should return `None`.
"""

from typing import Union, Tuple, Any

def inspect_dict_data(data: dict, descr: str, level: int = 1) -> Union[Tuple[str, Any], None]:
    for key, value in data.items():
        if value == descr:
            return key, value
        if isinstance(value, dict):
            result = inspect_dict_data(value, descr, level + 1)
            if result is not None:
                return result
    return None