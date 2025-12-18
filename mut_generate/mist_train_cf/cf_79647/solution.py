"""
QUESTION:
Write a function `longest_subseq(s, k, m)` that takes an alphanumeric string `s`, an integer `k`, and another integer `m` as input. The function should return the length of the longest subsequence within `s` where each alphabet's occurrence is not less than `k` and the total count of distinct alphabets in the subsequence is precisely `m`. The string `s` contains solely lowercase English alphabets and has a length between 1 and 10^4, inclusive. The value of `k` is between 1 and 10^5, inclusive, and the value of `m` is between 1 and 26, inclusive.
"""

from collections import Counter
from itertools import combinations

def longest_subseq(s, k, m):
    c = Counter(s)
    max_len = 0

    for combo in combinations(c, m):
        combo_counts = [c[char] for char in combo if c[char] >= k]
        if len(combo_counts) == m:
            curr_len = sum(combo_counts)
            if curr_len > max_len:
                max_len = curr_len

    return max_len