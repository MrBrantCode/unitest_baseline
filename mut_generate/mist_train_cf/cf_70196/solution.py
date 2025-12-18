"""
QUESTION:
Determine the time complexity in Big Theta notation of the recursive function T(n), where T(1) = 7 and T(n + 1) = 3n + T(n) for all integers n ≥ 1. Assume that the input size is n.
"""

def entrance(n):
    if n == 1:
        return 7
    else:
        return 3*n + entrance(n-1)