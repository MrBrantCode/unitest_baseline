"""
QUESTION:
Write a function `sum_of_multiples` that calculates the sum of multiples of 4 and 7 up to a given number `n` that is also a perfect square. Note that `n` is guaranteed to be greater than 1.
"""

def sum_of_multiples(n):
    perfect_squares = [i*i for i in range(1, int(n**0.5) + 1)]
    multiples = [i for i in range(1, n) if i % 4 == 0 or i % 7 == 0]
    return sum(multiples) - sum(square for square in perfect_squares if square < n)