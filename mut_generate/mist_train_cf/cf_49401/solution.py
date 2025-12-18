"""
QUESTION:
Write a function called `shortest_nested_string` that takes a nested list of strings as input and returns the last shortest string in the nested list. If there are multiple strings with the same shortest length, return the last one encountered. If the input list is empty, return `None`. The function should be able to handle nested lists of arbitrary depth.
"""

from typing import List, Optional, Any

def shortest_nested_string(strings: List[Any]) -> Optional[str]:
    if not strings:
        return None
    shortest_str = None
    for string in strings:
        if type(string) is list:
            string = shortest_nested_string(string)
        if shortest_str is None or (string is not None and len(string) <= len(shortest_str)):
            shortest_str = string
    return shortest_str