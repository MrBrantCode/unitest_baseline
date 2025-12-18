"""
QUESTION:
Write a function called `sum_of_powers` that takes two parameters `n` and `m` (with `m` defaulting to 0) and returns a tuple containing the sum of the fourth power of the first `n` odd natural numbers and the sum of the fourth power of the first `m` even natural numbers. The function should use recursion and have a time complexity of O(n + m).
"""

def sum_of_powers(n, m=0):
    if n == 0 and m == 0:
        return (0, 0) 
    elif n == 0:
        return (0, (m * (m + 1)) ** 2) 
    elif m == 0:
        return ((n * (2 * n - 1)) ** 2, 0) 
    else:
        return ((n * (2 * n - 1)) ** 2, (m * (m + 1)) ** 2)