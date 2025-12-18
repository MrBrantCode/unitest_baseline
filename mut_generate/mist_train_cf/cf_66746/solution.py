"""
QUESTION:
Write a function `is_happy_advanced(s, k)` that determines if a given string `s` is happy or not. A string is considered happy if its length is no less than `k`, each set of `k` sequential characters are unique, every distinct character occurs at least `k` times, and no `k` consecutive characters are the same.
"""

def entance(s, k):
    # check if string length is less than k
    if len(s) < k:
        return False
    
    # check if every distinct character occurs at least k times
    for char in set(s):
        if s.count(char) < k:
            return False
            
    # check if each set of k sequential characters are unique
    for i in range(len(s) - k + 1):
        if len(set(s[i: i+k])) < k:
            return False
    
    # check if no k consecutive characters are same
    for i in range(len(s) - k + 1):
        if len(set(s[i: i+k])) == 1:
            return False
        
    return True