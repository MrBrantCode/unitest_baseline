"""
QUESTION:
Extract all possible subsequences of a given length from a string.

Write a function `extract_subsequences(s, n)` that takes a string `s` and an integer `n` as input and returns a list of all possible subsequences of length `n` from the string. If the string's length is less than `n`, the function should return an empty list.
"""

def extract_subsequences(s, n):
    if len(s) < n:
        return []
    
    subsequences = []
    for i in range(len(s) - n + 1):
        subsequences.append(s[i:i+n])
    
    return subsequences