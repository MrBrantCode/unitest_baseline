"""
QUESTION:
Implement a function `cycpattern_check(a, b)` that checks if the second string `b` or any of its cyclic permutations exists as a contiguous subsequence within the first string `a`, disregarding case and special characters. The function should be efficient even with larger string sizes.
"""

import re
from collections import deque

def cycpattern_check(a, b):
    # Filter special characters and change strings to lowercase
    a = re.sub(r'\W+','', a).lower()
    b = re.sub(r'\W+','', b).lower()
    
    if len(a) < len(b): # if b is longer than a, it can't be a subsequence of a
        return False
    
    b_deque = deque(b) # use deque to achieve O(1) time complexity in rotation
    for _ in range(len(b)): # try every rotation
        if is_subsequence(''.join(list(b_deque)), a):
            return True
        b_deque.rotate(1) # rotate string b
    return False

def is_subsequence(b, a):
    i = j = 0
    while i < len(a) and j < len(b):  
        if a[i] == b[j]: 
            j += 1
        i += 1
    return j == len(b)