"""
QUESTION:
Create a function named `custom_blender` that takes three string parameters `s1`, `s2`, and `s3`, and returns a tuple containing a string and an integer. The function should intersperse characters from the input strings alternately, ignoring numeric characters and counting the number of bypassed characters. The output string should contain the non-numeric characters from the input strings in the order they appear, and the integer should be the count of bypassed characters.
"""

from typing import Tuple

def custom_blender(s1: str, s2: str, s3: str) -> Tuple[str, int]:
    """
    Intersperse characters from all three input strings alternately, ignore numeric characters and count the number of bypassed characters. 
    Output the final string and append the count of bypassed characters at the end.
    """
    res = []
    bypassed = 0
    strings = [iter(s) for s in [s1, s2, s3]]
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