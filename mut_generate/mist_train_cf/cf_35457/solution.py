"""
QUESTION:
Implement the function `count_characters(string, characters)` to count the occurrences of specific characters in a given string. The function should take a non-empty string `string` containing alphanumeric and non-alphanumeric characters, and a list of characters `characters` as input, and return the count of each character in the string. The function should ignore case sensitivity and non-alphabetic characters. 

The input parameters are:
- `string`: a non-empty string
- `characters`: a list of characters to count occurrences for

The function should return a dictionary where the keys are the characters from the input list and the values are their corresponding counts in the string.
"""

from collections import defaultdict
from typing import List, Dict

def count_characters(string: str, characters: List[str]) -> Dict[str, int]:
    string = string.lower()
    char_count = defaultdict(int)
    for char in string:
        if char.isalpha() and char in [c.lower() for c in characters]:
            char_count[char] += 1
    return dict(char_count)