"""
QUESTION:
Write a function named `harmonic_mean` that calculates the harmonic mean of three numbers. The function should take three numerical values as input and return the harmonic mean, calculated as 3 divided by the sum of the reciprocals of the input values. Assume the input values are non-zero.
"""

def harmonic_mean(a, b, c):
    return 3 / ((1/a) + (1/b) + (1/c))