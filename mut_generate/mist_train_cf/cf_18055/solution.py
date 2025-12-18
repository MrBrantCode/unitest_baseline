"""
QUESTION:
Write a function `print_consecutive_squares(N)` that takes an integer `N` as input and returns a list of all perfect square numbers between 1 and `N`. The function should also print the numbers from 1 to `N`. The function should be efficient for large values of `N`.
"""

import math

def print_consecutive_squares(N):
    squares = []
    
    for i in range(1, N+1):
        if math.isqrt(i)**2 == i:
            squares.append(i)
        print(i)
    
    return squares