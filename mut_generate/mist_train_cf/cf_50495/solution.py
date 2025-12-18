"""
QUESTION:
Create a function named `custom_concatenate` that takes a list of strings as input. The function should concatenate the strings in the list by interleaving characters from each string, then reversing the order of the strings. If the strings are of different lengths, the function should ignore the missing characters in the shorter strings. The function should return the concatenated string. The input list can be empty, in which case the function should return an empty string.
"""

from typing import List

def custom_concatenate(strings: List[str]) -> str:
    result = []
    max_len = max(len(s) for s in strings) if strings else 0
    for i in range(max_len):
        for s in reversed(strings):
            if i < len(s):
                result.append(s[i])
    return ''.join(result)