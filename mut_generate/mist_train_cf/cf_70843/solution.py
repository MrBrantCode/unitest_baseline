"""
QUESTION:
Construct a Python function called `is_subsequence` that takes two parameters: `string` and `sub`. The function should return a boolean value indicating whether the character sequence `sub` exists as a subsequence within the character sequence `string`. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. The function should not use any external libraries and should be efficient in terms of time complexity.
"""

def is_subsequence(string: str, sub: str) -> bool:
    sub_len = len(sub)
    string_len = len(string)
    i = 0
    j = 0

    while j < sub_len and i < string_len:
        if string[i] == sub[j]:
            j += 1
        i += 1

    return j == sub_len