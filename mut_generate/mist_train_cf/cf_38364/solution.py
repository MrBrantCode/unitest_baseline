"""
QUESTION:
Write a function `sum_of_n_mod_m(n: int) -> int` that takes an integer `n` as input, calculates the sum of the first `n` natural numbers modulo `10^9 + 7`, and returns the result. The function should use the formula for the sum of an arithmetic series to calculate the sum and handle the modulo operation to prevent overflow.
"""

def sum_of_n_mod_m(n: int) -> int:
    mod = 10**9 + 7
    total_sum = (n * (n + 1)) // 2  # Calculate the sum of the first n natural numbers
    return total_sum % mod  # Return the sum modulo mod