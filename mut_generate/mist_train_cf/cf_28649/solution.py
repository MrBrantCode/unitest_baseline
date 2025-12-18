"""
QUESTION:
You are given a dictionary `VALUE_MAP` containing nested dictionaries with `False` and `True` keys. Write a function `process_value_map` that takes a string `key` (1 <= len(key) <= 10) and a boolean `boolean_value`, and returns the value associated with the given key and boolean in the `VALUE_MAP`. If the key or boolean value is not present, return "Key or boolean not found".
"""

from typing import Union

VALUE_MAP = {
    "locked": {False: None, True: "not a None"},
    "fresh": {False: False, True: True},
    "remove": {False: set(), True: ("b", "a")},
    "update": {False: {}, True: {"y": 2.3, "x": 1, "z": "dummy"}},
}

def process_value_map(key: str, boolean_value: bool) -> Union[None, bool, set, tuple, dict, str]:
    if key in VALUE_MAP and boolean_value in VALUE_MAP[key]:
        return VALUE_MAP[key][boolean_value]
    else:
        return "Key or boolean not found"