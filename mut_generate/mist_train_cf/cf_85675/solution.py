"""
QUESTION:
Write a function `refined_cycpattern_check(a, b)` that determines if string `b` or any of its rotational permutations can form consecutive subsequences within string `a`. The function should ignore case sensitivity and exclude special characters during the subsequence examination. If a match is found, return `True` along with the starting and ending index of the subsequence in `a`. Otherwise, return `False` and `None`.
"""

import re

def refined_cycpattern_check(a, b):
    a = re.sub(r'\W+', '', a.lower())
    b = re.sub(r'\W+', '', b.lower())
    
    b_length = len(b)
    
    for i in range(b_length):
        rotate_b = b[i:] + b[:i]
        b_start = a.find(rotate_b)
        if b_start != -1:
            return True, (b_start, b_start+b_length-1)
            
    return False, None