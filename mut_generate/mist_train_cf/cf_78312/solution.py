"""
QUESTION:
Create a function named `custom_reverse_interleave` that takes a list of strings as input. The function should reverse the order of the characters in each string, then interleave the characters from the reversed strings in reverse order. If the strings are of different lengths, the remaining characters from the longer strings should be appended at the end. The function should return the resulting string.
"""

from typing import List

def custom_reverse_interleave(strings: List[str]) -> str:
    # Reverse every string in the list
    reversed_strings = [s[::-1] for s in strings]
    # Find the length of the longest string
    max_len = max(len(s) for s in reversed_strings) if reversed_strings else 0

    result = []
    for i in range(max_len):
        for string in reversed_strings:
            if i < len(string):
                result.append(string[i])

    # Join characters together to form the result string
    return ''.join(result)