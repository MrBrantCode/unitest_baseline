"""
QUESTION:
Write a function called `harmonic_mean` that takes three numbers as input and returns their harmonic mean. The function should be able to handle three distinct numbers and calculate the harmonic mean correctly, which is the total count of numbers divided by the sum of their reciprocals.
"""

def harmonic_mean(a, b, c):
    return 3 / ((1/a) + (1/b) + (1/c))