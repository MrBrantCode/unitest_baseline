"""
QUESTION:
Write a function `lucas_series(n)` that returns the nth element in the Lucas series, where the series starts with 2 and 1, and each subsequent element is the sum of the previous two. The function should also validate that the input `n` is a positive integer.
"""

def lucas_series(n):
    if not isinstance(n, int) or n < 1:
        return "The input has to be a positive integer."
    
    lucas = [2, 1]
    for i in range(2, n):
        lucas.append(lucas[i-1] + lucas[i-2])
        
    return lucas[n-1]