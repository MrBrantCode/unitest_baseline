"""
QUESTION:
Write a function named `process_dicts` that takes a list of dictionaries `dicts` and a string `key` as input. The function should extract the value of the specified `key` from each dictionary, convert it to an integer, and return a list of the converted values. If any dictionary does not contain the specified `key` or if the value cannot be converted to an integer, the function should return False. The input list of dictionaries contains at least one and at most 100 dictionaries.
"""

from typing import List, Dict, Any, Union

def process_dicts(dicts: List[Dict[str, Any]], key: str) -> Union[List[int], bool]:
    converted_values = []
    for d in dicts:
        if key in d:
            try:
                converted_values.append(int(d[key]))
            except ValueError:
                return False
        else:
            return False
    return converted_values