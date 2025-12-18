"""
QUESTION:
Create a function called `tuple_list_to_dict` that takes a list of tuples as input and returns a dictionary where the keys are the first elements of the tuples and the values are lists of the second elements of the tuples. If a key is already present in the dictionary, the corresponding value should be appended to the existing list. If a key is not present, a new key-value pair should be added to the dictionary.
"""

from typing import List, Tuple, Any, Dict

def tuple_list_to_dict(input_list: List[Tuple[Any, Any]]) -> Dict[Any, List[Any]]:
    out_dict = {}
    for key, value in input_list:
        if key in out_dict:
            out_dict[key].append(value)
        else:
            out_dict[key] = [value]
    return out_dict