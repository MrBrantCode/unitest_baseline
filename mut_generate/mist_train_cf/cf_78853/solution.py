"""
QUESTION:
Design a function `string_info` that takes a list of strings `input_list` and a target string `target` as input. The function should return a dictionary containing the first occurrence, last occurrence, a list of distinct strings, and a list of distinct strings that are anagrams of the target string. The function should be optimized for efficiency and should not consider the case when the target string is not found in the list.
"""

from typing import List
from collections import Counter

def string_info(input_list: List[str], target: str):
    first_occur = next((i for i, value in enumerate(input_list) if value == target), None)
    last_occur = len(input_list) - 1 - next((i for i, value in enumerate(reversed(input_list)) if value == target), None) if first_occur is not None else None
    distinct_strings = set(input_list)
    target_counter = Counter(target)
    anagram_strings = [s for s in distinct_strings if Counter(s) == target_counter and s != target]
    
    return {
        "first_occurrence": first_occur,
        "last_occurrence": last_occur,
        "distinct_strings": list(distinct_strings),
        "anagram_strings": anagram_strings,
    }