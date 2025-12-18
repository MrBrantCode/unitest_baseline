"""
QUESTION:
Write a function named `num_colourings` that takes an integer `n` as input, representing the number of available colours for a 2x2x2 Rubik's Cube, and returns the number of fundamentally different colourings considering rotational symmetry, where two colourings are considered fundamentally different if one cannot be transformed into the other by feasible Rubik's Cube maneuvers.
"""

import math

def num_colourings(n):
    total = 0
    total += n**24
    total += 3*math.factorial(4)*n**6
    total += math.factorial(3)*n**8
    total += 3*math.factorial(4)*n**12
    total += 6*n**(24/2)
    total += 8*(math.factorial(3)**2)*n**8
    total += 6*math.factorial(4)*math.factorial(2)*n**9
    return total/24