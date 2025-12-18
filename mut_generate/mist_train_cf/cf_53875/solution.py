"""
QUESTION:
Write a function `substrings_of_length(s, k, n)` that takes a string `s` and two integers `k` and `n` as input. The function should return the count of substrings of length `k` in `s` that do not contain any recurring characters and have at least `n` unique characters. The length of `s` is at least 1 and at most 10^4, all characters in `s` are lowercase English alphabets, the value of `k` is at least 1 and at most 10^4, and the value of `n` is at least 1 and at most `k`.
"""

def entance(s, k, n):
    result = set()
    for i in range(len(s) - k + 1):
        substr = s[i:i+k]
        if len(set(substr)) == len(substr) and len(set(substr)) >= n:
            result.add(substr)
    return len(result)