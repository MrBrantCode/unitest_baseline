"""
QUESTION:
Given two strings `input_str` and `pattern`, write a function `find_string_anagrams` that returns a list of indices where the anagrams of the `pattern` are found in the `input_str`. The function should handle cases where `input_str` or `pattern` is empty, or the length of `pattern` is greater than the length of `input_str`.
"""

from collections import Counter
from typing import List

def find_string_anagrams(input_str: str, pattern: str) -> List[int]:
    if not pattern or not input_str or len(pattern) > len(input_str):
        return []

    window_start, matched = 0, 0
    char_frequency = Counter(pattern)

    result = []
    for window_end in range(len(input_str)):
        right_char = input_str[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            result.append(window_start)

        if window_end >= len(pattern) - 1:
            left_char = input_str[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return result