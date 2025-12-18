"""
QUESTION:
Create a function `custom_concatenate(strings)` that takes a list of strings as input and returns a single string. The function should interleave the characters from the input strings, reverse the order of characters, and append any leftover characters from strings of varying lengths at the end. The input list may be empty, and the function should handle strings of different lengths.
"""

from typing import List

def custom_concatenate(strings: List[str]) -> str:
    # Convert the list of strings into list of characters
    strings = [list(s) for s in strings]

    # Initialize the final result as an empty string
    result = ''

    # Interleave the characters of the strings
    while strings:
        for s in strings:
            if s:
                result += s.pop()

        # Remove empty lists
        strings = [s for s in strings if s]

    # Return the final result
    return result