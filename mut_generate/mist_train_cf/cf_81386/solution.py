"""
QUESTION:
Implement a function `find_longest_string_sum` that takes a list of strings `strings` and a tuple of prefix and suffix `prefix_suffix` as input. The function should return a tuple containing the longest string in the list that starts with the specified prefix and ends with the specified suffix, and the cumulative sum of all characters in this longest string. Character values are computed as 'a'=1, 'b'=2, ..., 'z'=26, with no distinction made for capitalization. If no suitable strings are found, the function should return an empty string and a character sum of zero.
"""

from typing import List, Tuple
import string

def find_longest_string_sum(strings: List[str], prefix_suffix: Tuple[str, str]) -> Tuple[str, int]:
    longest_string = ""
    total_sum = 0

    # maps a-z to 1-26, useful for sum computation
    ch_to_int = {ch: idx for idx, ch in enumerate(string.ascii_lowercase, start=1)}

    for s in strings:
        if (s.lower().startswith(prefix_suffix[0].lower()) 
            and s.lower().endswith(prefix_suffix[1].lower()) 
                and len(s) >= len(longest_string)):

            # record the longest string and compute sum of its characters
            longest_string = s
            total_sum = sum(ch_to_int[ch] for ch in s.lower() if ch in ch_to_int)

    return longest_string, total_sum