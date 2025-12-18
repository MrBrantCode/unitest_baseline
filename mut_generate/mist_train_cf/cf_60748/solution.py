"""
QUESTION:
Create a function `count_pairs` that takes two integers `n` and `k` as input and returns the count of pairs of numbers `(i, j)` where `i` and `j` are in the range from 1 to `n` (inclusive), `i` is less than `j`, and the sum of `i` and `j` is less than `k`. Implement the function in a single line of code using a list comprehension and built-in Python functions.
"""

def count_pairs(n, k):
    return len([(i,j) for i in range(1, n+1) for j in range(i+1, n+1) if i + j < k])