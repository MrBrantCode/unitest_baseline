"""
QUESTION:
Write a function minFlipsMonotone(S) that takes a string S of '0's and '1's as input and returns the minimum number of flips to make S monotone increasing. The function can flip at most two consecutive '0's or '1's at a time. The length of S is between 1 and 20000 inclusive, and S only consists of '0' and '1' characters.
"""

def minFlipsMonotone(S: str) -> int:
    flips0 = 0
    flips1 = 0
    for c in S:
        if c == '1':
            flips1 = min(flips0, flips1)
            flips0 += 1
        else:
            flips1 = min(flips0, flips1) + 1
    return min(flips0, flips1)