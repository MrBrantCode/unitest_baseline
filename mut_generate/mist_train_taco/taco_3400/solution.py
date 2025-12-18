"""
QUESTION:
Ambar is a gardener and have many water jugs in his garden. 

The shape of water jug is a cone placed on the top of a cylinder (the radius and height of cylinder and cone and is "r").
There is a jug for each value of "r'. "r" varies from 1 to "n" ("n" being the input).

Help Ambar in finding the cumulative sum of  volumes.
Answer should be rounded off.

value of pi 3.141592653589793

Input :
100

NOTE : You do not need to create a program for this problem you have to write your answers of given input in given code snippet
To see how to submit solution please check this link

SAMPLE INPUT
1

SAMPLE OUTPUT
4
"""

import math

def calculate_cumulative_volume(n):
    pi = 3.141592653589793
    cumulative_volume = 0
    
    for r in range(1, n + 1):
        # Volume of the cylinder (V_cylinder = π * r^2 * h)
        # Volume of the cone (V_cone = (1/3) * π * r^2 * h)
        # Since the height of both the cylinder and cone is "r"
        volume = (pi * r**3) + ((1/3) * pi * r**3)
        cumulative_volume += volume
    
    # Round the cumulative volume to the nearest integer
    return round(cumulative_volume)