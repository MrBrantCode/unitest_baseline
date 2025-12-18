"""
QUESTION:
Write a function named `find_sum` that takes an integer `n` and returns the sum of all odd integers from 1 to `n`. The function must use recursion and cannot use loops, built-in sum functions, or additional variables to store intermediate results.
"""

def find_sum(n):
    if n <= 0:
        return 0
    elif n % 2 == 0:
        return find_sum(n-1)
    else:
        return n + find_sum(n-2)