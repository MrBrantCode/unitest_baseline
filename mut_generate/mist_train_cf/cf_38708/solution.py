"""
QUESTION:
Implement a function `countDistinctSubstrings` that takes a string `s` as input and returns the number of distinct substrings that can be formed from `s`. The function should count all possible contiguous sequences of characters within the string `s`. The input string `s` will contain only ASCII characters and its length will not exceed 10^5.
"""

def countDistinctSubstrings(s: str) -> int:
    substrings = set()
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            substrings.add(s[i:j+1])
    return len(substrings)