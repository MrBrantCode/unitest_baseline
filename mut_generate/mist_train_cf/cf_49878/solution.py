"""
QUESTION:
Write a function `find_longest_string_sum` that takes a list of strings, a tuple containing a prefix and a suffix, and a sequence as input. The function should return a tuple containing the longest string that starts with the given prefix, ends with the given suffix, and includes the given sequence, along with the sum of its characters where 'a' is 1, 'b' is 2, ..., 'z' is 26, and non-alphabetic characters are ignored. If there is a length tie, return the first longest string. If no suitable string is found, return an empty string and zero.
"""

from typing import List, Tuple, Union

def find_longest_string_sum(strings: List[str], prefix_suffix: Tuple[str, str], sequence: str) -> Union[str, int]:
    longest_string = ''
    longest_string_length = 0
    sum_longest = 0

    for s in strings:
        if s.startswith(prefix_suffix[0]) and s.endswith(prefix_suffix[1]) and sequence in s:
            if len(s) > longest_string_length:
                longest_string = s
                longest_string_length = len(s)

    if longest_string:
        sum_longest = sum(ord(i) - ord('a') + 1 for i in longest_string.lower() if 'a' <= i.lower() <= 'z')

    return longest_string, sum_longest