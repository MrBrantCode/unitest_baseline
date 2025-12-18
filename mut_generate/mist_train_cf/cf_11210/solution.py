"""
QUESTION:
Create a function called `calculate_e` that takes an integer `n` as input, representing the number of terms to calculate the value of "e" using the Taylor series expansion, where the input value `x` is always 1. The function should return the calculated value of "e" to the nth term.
"""

def calculate_e(n):
    e = 1
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i
        e += 1 / factorial

    return e