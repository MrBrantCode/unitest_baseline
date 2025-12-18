"""
QUESTION:
Create a function called `get_keys_sorted_by_value_length` that takes a dictionary as input and returns a list of its keys in descending order based on the length of their corresponding values. The function must handle values of any data type by converting them to strings before calculating their length.
"""

from typing import List, Dict

def get_keys_sorted_by_value_length(my_dict: Dict) -> List[str]:
    sorted_keys = sorted(my_dict.keys(), key=lambda x: len(str(my_dict[x])), reverse=True)
    return sorted_keys