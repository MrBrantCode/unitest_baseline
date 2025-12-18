"""
QUESTION:
Write a function `solve(N)` that calculates the sum of the digits of a given positive integer `N`, converts the sum into binary form, and returns the binary number as a string. The input integer `N` is within the range 0 to 10000.
"""

def entance(N):
    sum_of_digits = sum(int(digit) for digit in str(N))
    binary = bin(sum_of_digits)[2:]
    return binary