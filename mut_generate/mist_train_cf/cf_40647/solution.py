"""
QUESTION:
Implement the `find_valid_substrings` function which takes a string and a list of valid words as input, and returns a list of valid substrings found in the string according to the given dictionary. A valid word is defined as a sequence of characters that forms a word found in the dictionary. The function should iterate through all possible substrings of the input string and check if each substring is a valid word. If a valid word is found, it should be added to the list of valid substrings to be returned. The input string has a length between 1 and 1000, and the dictionary has a length between 1 and 1000.
"""

from typing import List

def find_valid_substrings(s: str, words: List[str]) -> List[str]:
    found = set()
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if substring in words:
                found.add(substring)
    return list(found)