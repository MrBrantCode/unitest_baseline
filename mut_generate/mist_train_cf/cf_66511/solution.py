"""
QUESTION:
Write a function `subfactorial(n)` that calculates the number of derangements of `n` distinct items. The function should not take any additional inputs other than `n` and should return an integer. The function should be able to handle the case where `n = 10`. Note that there's no standard function in Python to find the subfactorial, so the function should be computed using its formula: `!n = n! * (1 - 1/1! + 1/2! - 1/3! + ... + (-1)^n/n!)`.
"""

import math

def subfactorial(n):
    sum = 0
    fact = math.factorial(n)
    for i in range(n+1):
        if i % 2 == 0:
            sum += fact / math.factorial(i)
        else:
            sum -= fact / math.factorial(i)
    return int(sum)