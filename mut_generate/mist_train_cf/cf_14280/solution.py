"""
QUESTION:
Write a function `lucas` to compute the nth Lucas number, where Lucas numbers are defined as L(n) = L(n-1) + L(n-2) for n > 1, L(0) = 2, and L(1) = 1. Also, write a function `sum_of_cubes` that calculates the sum of the cubes of the first n Lucas numbers.
"""

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)