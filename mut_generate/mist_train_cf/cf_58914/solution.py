"""
QUESTION:
Write a function `accumulate_on_condition(n, condition)` that takes two parameters: an integer `n` where 1 < n < 10^5, and a function `condition` that returns a boolean when given an integer. The function should return the accumulated total of integers from 1 to `n` (inclusive) that satisfy the condition.
"""

def accumulate_on_condition(n, condition):
    total = 0
    for i in range(1, n+1):
        if condition(i):
            total += i
    return total