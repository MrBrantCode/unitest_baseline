"""
QUESTION:
Write a function `extract_subsequences(s, n)` that takes a string `s` and an integer `n` as input, and returns a list of all possible subsequences of length `n` from the string `s`. The subsequences should be extracted in the order they appear in the string.
"""

def extract_subsequences(s, n):
    subsequences = []
    for i in range(len(s) - n + 1):
        subsequence = s[i:i+n]
        subsequences.append(subsequence)
    return subsequences