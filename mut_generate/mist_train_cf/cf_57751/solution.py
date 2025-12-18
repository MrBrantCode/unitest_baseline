"""
QUESTION:
Implement the function `fast_algo(n)` that calculates the sum of all integers from 1 to n and optimizes its performance for large inputs. The function should take an integer `n` as input and return the sum as an integer. The optimized function should have a better time complexity than the naive approach of iterating over all integers up to n. Measure and compare the execution time of the optimized function with the original function for a large input to demonstrate the speed improvement.
"""

def fast_algo(n):
    return n*(n+1)//2