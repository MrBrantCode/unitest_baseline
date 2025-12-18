"""
QUESTION:
Calculate the value of Euler's number to a given precision using the infinite series definition, considering the limitations of floating point arithmetic. Implement a function `calculate_e(precision)` that takes an integer `precision` as input, representing the desired number of decimal places, and returns Euler's number rounded to the specified precision.
"""

import math

def calculate_e(precision):
    e = 0
    i = 0
    while True:
        old_e = e
        e += 1 / math.factorial(i)
        if e - old_e < 10**-precision:
            break
        i += 1
    return round(e, precision)