"""
QUESTION:
Given a string `str1` and a pattern `pattern`, implement a function `find_anagrams(str1: str, pattern: str) -> List[int]` that returns a list of starting indices of the anagrams of the pattern in the string. The function should return all indices where an anagram of the pattern appears in the string, including overlapping anagrams.
"""

from typing import List

def find_anagrams(str1: str, pattern: str) -> List[int]:
    result_indexes = []
    char_frequency = {}
    for char in pattern:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    window_start = 0
    matched = 0

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            result_indexes.append(window_start)

        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return result_indexes