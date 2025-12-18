"""
QUESTION:
Create a function `lucas(n)` that calculates the nth Lucas number, a sequence where each number is the sum of the two preceding ones, starting with 2 and 1.
"""

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1

    lucas_n_minus_1 = 2
    lucas_n_minus_2 = 1

    for _ in range(2, n + 1):
        lucas_n = lucas_n_minus_1 + lucas_n_minus_2
        lucas_n_minus_2 = lucas_n_minus_1
        lucas_n_minus_1 = lucas_n

    return lucas_n