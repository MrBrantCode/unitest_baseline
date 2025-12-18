"""
QUESTION:
Write a function `count_characters_in_string` that takes a string `input_string` and an optional dictionary `lookup_dict` as arguments. The function should return a tuple of two elements: the first one is a dictionary with the count of only alphabetic characters in the string, and the second one is a dictionary tracking the count of provided characters within the string if `lookup_dict` is provided. If `lookup_dict` is not provided, the second element of the returned tuple should be `None`. The function should have a time complexity of O(n), where n is the length of the `input_string`.
"""

from typing import Dict, Optional, Tuple

def count_characters_in_string(input_string: str, lookup_dict: Optional[Dict[str, int]]=None) -> Tuple[Dict[str, int], Optional[Dict[str, int]]]:
    count_dict = {}
    lookup_count = {}

    for char in input_string:
        if char.isalpha():
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
        if lookup_dict and char in lookup_dict:
            if char in lookup_count:
                lookup_count[char] += 1
            else:
                lookup_count[char] = 1

    if not lookup_dict:
        lookup_count = None

    return count_dict, lookup_count