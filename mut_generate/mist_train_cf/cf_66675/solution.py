"""
QUESTION:
Implement a function `custom_concatenate(strings)` that takes a list of strings as input and returns a single string. The function should interleave characters from the input strings in reverse order, remove any vowels, and then reverse the resulting string.
"""

from typing import List

def custom_concatenate(strings: List[str]) -> str:
    result = []
    # Iterate over the strings in reverse order
    for s in reversed(strings):
        # Iterate over the characters in each string in reverse order
        for c in reversed(s):
            # Skip vowels
            if c.lower() in "aeiou":
                continue
            # Append non-vowel characters to the result
            result.append(c)
    # Join the characters in the result to form a single string and return it
    return "".join(result)