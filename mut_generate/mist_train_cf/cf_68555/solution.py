"""
QUESTION:
Implement a function `calculate_geometric_sum(r, a=2, b=6)` that calculates the sum of a geometric series with ratio `r` and exponents ranging from `a` to `b` (inclusive), handling potential overflow errors and excluding ratios of 0 and 1.
"""

def calculate_geometric_sum(r, a=2, b=6):
    # check if the ratio is 0 to avoid divide by zero error
    if r == 0: 
        return "Error: The ratio cannot be 0."
    # check if the ratio is 1 to avoid infinite series
    elif r == 1: 
        return "Error: The ratio cannot be 1."
    else:
        try:
            return sum([r**(-i) for i in range(a, b+1)])
        except OverflowError:
            return "Error: Result is too large to be calculated."