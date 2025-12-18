"""
QUESTION:
Construct a function named `canConstruct` that takes a string `s` and an integer `k` as input, and returns a boolean value indicating whether it is feasible to use all the characters in `s` to construct `k` non-empty palindrome strings.

The length of `s` is between 1 and 10^5, and all characters in `s` are lower-case English letters. The integer `k` is between 1 and 10^5.
"""

from collections import Counter

def canConstruct(s: str, k: int) -> bool:
    if len(s) < k:
        return False
    counter = Counter(s)
    odd_count = sum(v % 2 for v in counter.values())
    return odd_count <= k