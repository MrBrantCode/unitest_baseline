"""
QUESTION:
Write a function `beautySum(s: str, k: int) -> int` that calculates the sum of beauty of all substrings of length `k` in string `s` that have all unique characters. The beauty of a string is the difference in frequencies between the most frequent and least frequent characters. The string `s` consists of only lowercase English letters and `1 <= s.length, k <= 500` and `1 <= k <= s.length`.
"""

def beautySum(s: str, k: int) -> int:
    return sum(len(set(s[i:i+k])) == k for i in range(len(s) - k + 1))