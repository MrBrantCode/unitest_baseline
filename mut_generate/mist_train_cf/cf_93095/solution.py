"""
QUESTION:
Write a function `extract_subsequences(s, n)` that takes a string `s` and an integer `n` as input and returns a list of all possible subsequences of length `n` from the string `s`. The function should return an empty list if the length of `s` is less than `n`.
"""

def extract_subsequences(s, n):
    if len(s) < n:
        return []
    
    subsequences = []
    for i in range(len(s) - n + 1):
        subsequences.append(s[i:i+n])
    
    return subsequences