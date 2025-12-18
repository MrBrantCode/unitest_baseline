"""
QUESTION:
Write a function `powers_of_two` that takes an integer `n` as input and returns a list of the first `n+1` powers of two, using recursion. The function should start with 1 (2^0) and end with 2^n.
"""

def entance(n):
    if n == 0:
        return [1]
    else:
        prev_powers = entance(n - 1)
        current_power = prev_powers[-1] * 2
        return prev_powers + [current_power]