"""
QUESTION:
Write a function `find_pythagorean_quadruplets(y)` that accepts a positive integer `y` and returns the smallest Pythagorean quadruplet (a, b, c, d) where a^2 + b^2 + c^2 = d^2 and a + b + c + d = y, along with the count of all possible quadruplets. The function should validate the input for edge cases like negative values and non-integer inputs, and handle large inputs efficiently.
"""

import numpy as np

def find_pythagorean_quadruplets(y):
    if (isinstance(y, int) == False or y <= 0):
        return "Invalid input. Please input a positive integer."

    quadruplets = []
    for a in range(1, int(np.cbrt(y/4))+1):
        for b in range(a, int(np.sqrt(y/3))+1):
            for c in range(b, int(np.sqrt(y/2))+1):
                d = y - a - b - c
                if a**2 + b**2 + c**2 == d**2:
                    quadruplets.append([a, b, c, d])

    if quadruplets:
        smallest_quadruplet = min(quadruplets, key=sum)
        return f"Smallest Pythagorean quadruplet is {smallest_quadruplet} and the total number of possible quadruplets are {len(quadruplets)}."
    else:
        return "No Pythagorean quadruplets found."