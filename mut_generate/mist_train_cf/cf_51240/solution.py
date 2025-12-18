"""
QUESTION:
Develop a function `filter_and_count_by_prefix_suffix` that filters a list of strings by different sets of prefixes and suffixes provided in a dictionary, and returns a dictionary with count of strings that passed the filter for every prefix-suffix combination. The input parameters are a list of strings and a dictionary where keys represent prefix and suffix combinations and values are tuples of prefixes and suffixes. The function should return a dictionary where keys are prefix and suffix combinations and values are tuples containing a list of strings that start with a certain prefix and end with a certain suffix, and the count of these strings. The function should achieve a time complexity of O(n log n) or better.
"""

from typing import Dict, List, Tuple

def filter_and_count_by_prefix_suffix(strings: List[str], prefix_suffix: Dict[str, Tuple[str, str]]) -> Dict[str, Tuple[List[str], int]]:
    result = dict()
    for k, (prefix, suffix) in prefix_suffix.items():
        filtered_strings = [s for s in strings if s.startswith(prefix) and s.endswith(suffix)]
        result[k] = (filtered_strings, len(filtered_strings))
    return result