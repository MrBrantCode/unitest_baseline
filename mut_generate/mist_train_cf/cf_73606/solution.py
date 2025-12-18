"""
QUESTION:
Write a function `numSubstrings(s: str) -> int` that takes a string `s` composed only of 'a', 'b', or 'c' characters and returns the cumulative count of substrings that encompass at least one occurrence of each of these characters. The length of `s` is between 3 and 5 x 10^4.
"""

def numSubstrings(s: str) -> int:
    a = b = c = -1
    counter = 0
    for i in range(len(s)):
        if s[i] == 'a':
            a = i
        elif s[i] == 'b':
            b = i
        elif s[i] == 'c':
            c = i
        counter += min(a, b, c) + 1 if a != -1 and b != -1 and c != -1 else 0
    return counter