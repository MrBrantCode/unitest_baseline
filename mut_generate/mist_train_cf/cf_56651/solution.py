"""
QUESTION:
Design a function `custom_concatenate` that takes a list of strings as input and returns a single concatenated string. The function should interleave characters from the input strings, reversing the order of characters from each string in the process, and then concatenate them. If the input list is empty, the function should return an empty string. The function should be able to handle strings of varying lengths.
"""

from typing import List

def custom_concatenate(strings: List[str]) -> str:
    if not strings:
        return ""
    
    max_len = max(len(s) for s in strings)
    result = []

    for i in range(max_len):
        for s in strings:
            if len(s) > i:
                result.append(s[-(i + 1)])
    
    return ''.join(result)