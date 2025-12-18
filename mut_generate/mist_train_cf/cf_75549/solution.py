"""
QUESTION:
Create a function `master_theorem(a, b, c)` that calculates the time complexity using the Master Theorem, given the number of subproblems `a`, the ratio of the problem size `b`, and the exponent of the work done outside recursive calls `c`. The function should return the time complexity in Big O notation and consider the restrictions that `a` and `b` must be greater than or equal to 1.
"""

import math

def master_theorem(a, b, c):
    if a < 1 or b < 1:
        return 'Both a and b must be greater than or equal to 1'
    
    log_result = math.log(a, b)
    
    if c < log_result:
        return "T(n) = Theta(n^%.2f)" % log_result
    elif c == log_result:
        return "T(n) = Theta(n^%.2f log n)" % log_result
    else:
        return "T(n) = Theta(n^%.2f)" % c