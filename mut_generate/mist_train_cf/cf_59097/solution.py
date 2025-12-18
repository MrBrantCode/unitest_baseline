"""
QUESTION:
Given an array of strings `arr` containing only lowercase English letters, write a function `maxLength` that returns the maximum possible length of a concatenated string `s` formed by a sub-sequence of `arr` with unique characters, where the sub-sequence must be in the same order as they appear in `arr`. The function should handle arrays with 1 to 16 strings, each with a length of 1 to 26 characters.
"""

def maxLength(arr):
    dp = [set()]
    for a in arr:
        if len(set(a)) < len(a): 
            continue
        a = set(a)
        for c in dp[:]:
            if a & c: 
                continue
            dp.append(a | c)
    return max(len(a) for a in dp)