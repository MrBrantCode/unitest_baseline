"""
QUESTION:
Implement a function named `count_occurrences(S, p)` to find the total number of non-overlapping occurrences of a pattern `p` in a string `S`. Both `S` and `p` consist of lowercase letters. The length of `p` is at least 2 and has no repeated letters. The length of `S` is at most 10^5 and the length of `p` is at most 10^3.
"""

def count_occurrences(S, p):
    count = 0
    n = len(S)
    m = len(p)
    
    i = 0
    while i < n:
        if S[i:i+m] == p:
            count += 1
            i += m
        else:
            i += 1
    
    return count