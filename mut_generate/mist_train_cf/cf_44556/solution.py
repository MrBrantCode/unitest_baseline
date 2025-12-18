"""
QUESTION:
Write a function `harmonic_mean(n1, n2, n3)` that calculates the harmonic mean of three numbers. The function should take three numbers as input and return the harmonic mean if all numbers are positive and non-zero. If any of the numbers are not valid, the function should return an error message.
"""

def harmonic_mean(n1, n2, n3):
    if n1 > 0 and n2 > 0 and n3 > 0:
        hm = 3 / ((1/n1) + (1/n2) + (1/n3))
        return hm
    else:
        return "Invalid: All numbers must be positive and non-zero."