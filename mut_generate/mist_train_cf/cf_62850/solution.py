"""
QUESTION:
Write a function `sum_multiples(a, b, limit)` that calculates the sum of all multiples of `a` and `b` between 1 and `limit`. The function should be able to handle any two given numbers `a` and `b`, and any given `limit`.
"""

def sum_multiples(a, b, limit):
    sum = 0
    for i in range(1, limit):
        if i % a == 0 or i % b == 0:
            sum += i
    return sum