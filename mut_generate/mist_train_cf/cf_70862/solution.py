"""
QUESTION:
Write a function `lcm(w: int, x: int, y: int, z: int) -> int` that calculates the Least Common Multiple (LCM) of four numbers `w`, `x`, `y`, and `z`. The function should be optimized for large inputs and should handle numbers within the range `1 <= w, x, y, z <= 10^9`.
"""

import math

def lcm(w: int, x: int, y: int, z: int) -> int:
    # function to calculate gcd
    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a%b
        return a

    # function to calculate lcm
    def lcm_two_numbers(a: int, b: int) -> int:
        return a*b // gcd(a, b)

    # finding lcm of four numbers 
    temp = lcm_two_numbers(w, x)
    temp = lcm_two_numbers(y, temp)
    result = lcm_two_numbers(z, temp)

    return result