"""
QUESTION:
Implement a function named `golden_ratio(precision)` that approximates the Golden Ratio using the continued fraction approach and takes an optional parameter `precision` (default value of 100) to control the number of recursive cycles for the approximation. The function should return the approximated value of the Golden Ratio.
"""

def golden_ratio(precision=100):
    def inner(cycles):
        if cycles == 0:
            return 1
        else:
            return 1 + 1/inner(cycles-1)
    return inner(precision)