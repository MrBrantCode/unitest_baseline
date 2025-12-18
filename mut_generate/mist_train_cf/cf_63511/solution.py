"""
QUESTION:
Implement the function `filter_by_prefix_and_suffix(strings: List[str], prefix_suffix: Tuple[str, str]) -> List[str]` to filter a list of strings that start with the prefix and end with the suffix from the `prefix_suffix` tuple and return them in a list sorted by their length.
"""

from typing import List, Tuple

def entance(strings: List[str], prefix_suffix: Tuple[str, str]) -> List[str]:
    """ 
    Implement a filtration process on a list of string entities, 
    accepting only those that start with a prefix and end with a suffix, 
    but also sequence them based on their length. 
    """
    filtered_sorted_strings = sorted([st for st in strings if st.startswith(prefix_suffix[0]) and st.endswith(prefix_suffix[1])], key=len)
    return filtered_sorted_strings