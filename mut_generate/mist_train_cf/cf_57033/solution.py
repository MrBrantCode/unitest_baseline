"""
QUESTION:
Write a function `find_longest_string_sum(strings, prefix_suffix)` that takes a list of strings `strings` and a tuple `prefix_suffix` containing a prefix and a suffix, and returns a tuple containing the longest string that starts with the prefix and ends with the suffix, and the sum of its characters (where 'a' or 'A' is 1, 'b' or 'B' is 2, ..., 'z' or 'Z' is 26). If multiple strings have the same maximum length, return the first one encountered. If no string matches the prefix and suffix, return an empty string and 0.
"""

from typing import List, Tuple, Union

def find_longest_string_sum(strings: List[str], prefix_suffix: Tuple[str, str]) -> Union[Tuple[str, int], Tuple[str, int]]:
    prefix, suffix = prefix_suffix
    longest_string = ('', 0)

    for string in strings:
        if string.startswith(prefix) and string.endswith(suffix) and len(string) > len(longest_string[0]):
            longest_string = (string, sum((ord(char.lower()) - 96) for char in string))

    return longest_string