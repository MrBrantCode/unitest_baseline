"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given number `n`, handling inputs up to 10000 without exceeding the recursion limit. The function should utilize a technique that minimizes stack space consumption for each recursive call. The function should also have an optional `result` parameter with a default value of 1 to store the intermediate result.
"""

import sys

sys.setrecursionlimit(10**6)  # Set recursion limit to a larger value

def entance(n, result=1):
    if n == 0:
        return result
    else:
        return entance(n-1, result*n)