"""
QUESTION:
Write a function `calculate_years` that calculates the number of years it takes for an amount of money to grow to a target amount at a certain interest rate compounded annually. The interest rate is such that an initial amount of $5000 doubles in 6 years. The function should take the principal amount `P` and the target amount `A` as inputs, and return the number of years `n` as output.
"""

from math import log

def calculate_years(principal, target):
    rate = (2 ** (1/6)) - 1
    return round(log(target/principal) / log(1 + rate))