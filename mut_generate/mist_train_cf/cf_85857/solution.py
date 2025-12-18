"""
QUESTION:
Write a function called `find_smallest_subsequence` that takes a string `s` as input and returns the smallest subsequence that repeats at least once in `s`. The function should return an empty string if no repeating subsequence is found.
"""

def find_smallest_subsequence(s):
    length = len(s)
    for size in range(1, length):
        for start in range(0, length):
            if start + size * 2 > length:
                break
            subseq = s[start : start + size]
            if s.count(subseq) > 1:
                return subseq
    return ""