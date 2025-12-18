"""
QUESTION:
Create a function named `lucas` that calculates the nth number in the Lucas series. The Lucas series starts with 2 and 1, and each subsequent number is the sum of the two preceding ones. Implement this function using recursion. The function should take one argument, `n`, representing the position of the number in the series, and return the corresponding value.
"""

def lucas(n): 
    if n == 0: 
        return 2
    elif n == 1: 
        return 1
    else: 
        return lucas(n-1) + lucas(n-2)