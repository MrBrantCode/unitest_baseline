"""
QUESTION:
Design a function `IsPerfectCubeSquareFibonacci (startnum, endnum)` that identifies and counts Fibonacci numbers within the defined range of `startnum` to `endnum` that are simultaneously perfect squares and perfect cubes. The function should handle only integer Fibonacci numbers, and return the quantity of such numbers that satisfy the conditions.
"""

import math

def IsPerfectCubeSquareFibonacci(startnum, endnum):
    a, b = 0, 1
    count = 0
    while a <= endnum:
        if a >= startnum:
            root = math.isqrt(a)
            cuberoot = round(a ** (1. / 3.))
            if root * root == a and cuberoot * cuberoot * cuberoot == a:
                count += 1
        a, b = b, a + b
    return count