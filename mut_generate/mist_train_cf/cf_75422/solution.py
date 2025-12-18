"""
QUESTION:
Compose a custom error-function named `custom_concatenate` that takes a list of strings as input and returns a concatenated string. The function should interleave characters from the input strings and then reverse the result. If the input strings vary in length, the remaining characters should be appended at the end. The function should also handle erroneous input by filtering out non-string types from the list.
"""

from typing import List
import itertools

def custom_concatenate(strings: List[str]) -> str:
    result = []

    strings = [s for s in strings if isinstance(s, str)]
    
    for c in itertools.zip_longest(*strings, fillvalue=''):
        result.extend(c[::-1])

    return ''.join(result)[::-1]