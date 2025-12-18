"""
QUESTION:
Create a function named `custom_mix_strings` that takes two parameters `s1` and `s2`, both of which are strings of the same length. The function should return a string that is created by intertwining `s1` and `s2` by swapping their characters, reversing the resulting string, and then capitalizing every other character.
"""

from typing import Tuple

def custom_mix_strings(s1: str, s2: str) -> str:
    # Ensure that both strings are of the same length
    assert len(s1) == len(s2), "Both strings should be of the same length"

    # Intertwine the strings
    intertwined = ''.join([j + i for i, j in zip(s1, s2)])

    # Reverse the string
    reversed_str = intertwined[::-1]

    # Capitalize every other character
    final_str = ''.join([char.upper() if idx % 2 == 0 else char.lower() for idx, char in enumerate(reversed_str)])

    return final_str