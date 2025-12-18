"""
QUESTION:
Write a function `print_consecutive_squares(N)` that takes an integer `N` as input and prints all consecutive numbers between 1 and `N`. The function should also identify and store perfect square numbers within the range. It should then return a list of all perfect square numbers between 1 and `N`. The function should be efficient enough to handle large values of `N`.
"""

import math

def print_consecutive_squares(N):
    squares = []
    
    for i in range(1, N+1):
        if math.isqrt(i)**2 == i:
            squares.append(i)
        print(i)
    
    return squares