"""
QUESTION:
Determine the growth rate 'r' in the exponential growth model A = Pe^(rt), where A is the final amount of fungi (750), P is the initial amount of fungi (100), and t is the time in hours (5). The function should calculate and return the precise value of 'r'.
"""

import math

def growth_rate(A, P, t):
    # rearrange the equation to solve for r
    r = math.log(A/P) / t
    return r