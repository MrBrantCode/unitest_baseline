"""
QUESTION:
Write a function `beneficial_partitions(s)` that calculates the quantity of beneficial divisions of a string `s` into two non-empty substrings `p` and `q` such that their concatenation equals `s` and the quantity of unique characters in `p` and `q` are identical.

The input string `s` consists only of lowercase English alphabets and has a length between 1 and 10^5 (inclusive). The function should return the total count of beneficial divisions.
"""

def beneficial_partitions(s):
    if not s: return 0
    
    n = len(s)
    beneficial_divisions = 0
    
    prefix_ways = [0]*n
    suffix_ways = [0]*n
    prefix_set = set()
    suffix_set = [set() for _ in range(n)]
    
    for i in range(n):
        prefix_set.add(s[i])
        prefix_ways[i] = len(prefix_set)
    
    for i in reversed(range(n)):
        suffix_set[i] = suffix_set[i+1].copy() if i+1 < n else set()
        suffix_set[i].add(s[i])
        suffix_ways[i] = len(suffix_set[i])
        
    for i in range(n-1):
        if prefix_ways[i] == suffix_ways[i+1]:
            beneficial_divisions += 1
            
    return beneficial_divisions