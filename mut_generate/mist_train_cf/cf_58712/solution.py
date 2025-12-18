"""
QUESTION:
Write a function `accumulate_numbers(n)` that uses recursion to calculate the sum of all numbers from 1 to n (inclusive). The function should take an integer `n` as a parameter, and it should be designed with efficiency of computation and algorithmic complexity in mind.
"""

def accumulate_numbers(n):
    # Base Case for recursion: If n equals to 0 or less, end the recursion
    if n <= 0:
        return 0
    else:
        return n + accumulate_numbers(n-1)