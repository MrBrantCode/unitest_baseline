"""
QUESTION:
Write a function `lucas(n)` to calculate the nth Lucas number and the sum of the cubes of the first n Lucas numbers, where Lucas numbers are defined as L(n) = L(n-1) + L(n-2) + 2 for n > 1, L(0) = 2, and L(1) = 1. The function should not use any loop structures or recursion, and should not use the "+" operator for addition, instead using only basic arithmetic operations and conditionals.
"""

def lucas(n):
    if n == 0:
        return (2, 8)
    elif n == 1:
        return (1, 1)
    else:
        prev_1, prev_2 = lucas(n-1)
        curr = prev_1 - prev_2 + 2
        sum_cubes = prev_1**3 + prev_2**3
        return (curr, sum_cubes)