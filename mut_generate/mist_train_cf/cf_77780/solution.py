"""
QUESTION:
Construct a function named `custom_blender` that takes two input strings `s1` and `s2` and returns a tuple containing the blended string and the count of bypassed characters. The function should alternate characters from both strings, ignoring numeric characters and keeping a count of such bypassed characters. The blended string should be in the original order of insertion, followed by the count of bypassed characters. Ensure the function handles cases where one or both strings are empty.
"""

from typing import Tuple

def custom_blender(s1: str, s2: str) -> Tuple[str, int]:
    bypass_count = 0
    result = []

    i = j = 0
    while i<len(s1) or j<len(s2):
        if i<len(s1):
            if  not s1[i].isdigit():
                result.append(s1[i])
            else:
                bypass_count += 1
            i += 1
        
        if j<len(s2):
            if not s2[j].isdigit():
                result.append(s2[j])
            else:
                bypass_count += 1
            j += 1

    return "".join(result), bypass_count