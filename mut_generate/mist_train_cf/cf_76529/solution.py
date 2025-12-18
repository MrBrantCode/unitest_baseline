"""
QUESTION:
Write a function `countSubstrings(s)` that takes a string `s` as input and returns the number of palindromic substrings of `s` with a length greater than 1 and consisting of more than one distinct character. The input string `s` is guaranteed to have a length of at most 1000.
"""

def countSubstrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):  
            substr = s[i: j]
            if substr == substr[::-1] and len(set(substr)) > 1: 
                count += 1
    return count