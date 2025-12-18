"""
QUESTION:
Write a function `identifyQuadrilateral(p, q, r, s)` that determines the type of quadrilateral represented by the 4 sides of lengths p, q, r, and s, assuming right angles between each pair of adjacent sides. The function should handle both integer and floating point inputs accurately and return the type of quadrilateral as 'Rectangle', 'Square', or 'Unknown'.
"""

def identifyQuadrilateral(p, q, r, s):
    if p == q and q == r and r == s:
        return 'Square'
    elif (p == q and r == s) or (p == r and q == s) or (p == s and q == r):
        return 'Rectangle'
    else:
        return 'Unknown'