"""
QUESTION:
Write a function `recursive_sum(n, memo={})` that calculates the sum of all numbers from 1 to `n` using memoization to optimize the recursive calculation and prevent redundant calculations. The function should take an integer `n` and an optional dictionary `memo` as parameters and return the sum of all numbers from 1 to `n`. The function should store the results of expensive function calls and reuse them when the same inputs occur again to achieve a time complexity of O(n).
"""

def recursive_sum(n, memo={}):
    if n in memo:             # check if the result has been calculated before
        return memo[n]
    elif n == 0:
        memo[0] = 0           # base case where n is zero
        return 0
    else:                     # if result has not been calculated before
        result = n + recursive_sum(n-1, memo)
        memo[n] = result      # store the result in the dictionary 'memo'
        return result