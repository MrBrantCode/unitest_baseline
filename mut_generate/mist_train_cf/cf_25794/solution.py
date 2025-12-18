"""
QUESTION:
Write a function `sum_multiples(n)` that calculates the sum of all the multiples of 3 and 5 below a given number `n`. The input `n` is an integer and the multiples are considered within the range (0, n).
"""

def sum_multiples(n):
    result = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result