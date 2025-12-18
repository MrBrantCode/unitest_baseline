"""
QUESTION:
Create a function `custom_mix_strings(s1: str, s2: str) -> str` that intertwines two strings of non-equal length by alternating their characters, starting with the longer string, and then reverses the result.
"""

from itertools import zip_longest

def custom_mix_strings(s1: str, s2: str) -> str:
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    intertwined_string = ''.join(x+y for x, y in zip_longest(s1, s2, fillvalue=''))
    return intertwined_string[::-1]