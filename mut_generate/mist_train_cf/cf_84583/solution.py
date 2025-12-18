"""
QUESTION:
Create a function `custom_blender` that takes three input strings `s1`, `s2`, and `s3` and returns a tuple containing a string and an integer. The function should interleave characters from the input strings alternately, bypassing any numeric characters found and keeping a count of these bypassed characters. The function should return the interleaved string with the bypassed numeric characters in their original order and append the count of bypassed numeric characters at the end.
"""

from typing import Tuple

def custom_blender(s1: str, s2: str, s3: str) -> Tuple[str, int]:
    """
    Interleave characters from all three input strings alternately, ignore numeric characters and count the number of bypassed characters. Output the final string and append the count of bypassed characters at the end.
    """
    res = []
    bypassed = 0
    strings = [iter(s) for s in (s1, s2, s3)]
    while strings:
        for s in strings[:]:
            try:
                c = next(s)
                if c.isnumeric():
                    bypassed += 1
                else:
                    res.append(c)
            except StopIteration:
                strings.remove(s)
    return ''.join(res), bypassed