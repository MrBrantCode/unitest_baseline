"""
QUESTION:
Calculate the minimum number of leaps of a specified length needed to arrive at a coordinate of the form (d, 0) from the origin in a Cartesian plane. The function should accommodate scenarios where the leap length does not evenly divide the distance 'd' and yield the least number of leaps necessary to reach or exceed the coordinate (d, 0). 

Implement a function `calc_leaps(d, leap_length)` that takes two parameters: `d` (the distance to be covered) and `leap_length` (the length of each leap), and returns the minimum number of leaps required. The function should be able to handle cases where `leap_length` does not evenly divide `d`.
"""

import math

def calc_leaps(d, leap_length):
    return math.ceil(d/leap_length)