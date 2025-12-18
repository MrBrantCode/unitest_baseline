"""
QUESTION:
Design a function named `unique_fusion` that takes a list of strings as input and returns a single string. The function should merge each string in the list into a single string, reversing every other string. The reversal starts with the first string, so the first, third, fifth, etc. strings are reversed. The function should handle lists of any length and should not modify the original list.
"""

from typing import List

def unique_fusion(l: List[str]) -> str:
    return ''.join(word[::-1] if i%2==0 else word for i, word in enumerate(l))