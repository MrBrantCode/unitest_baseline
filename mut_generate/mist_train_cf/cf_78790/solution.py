"""
QUESTION:
Given a box containing an equal number of white and black balls, write a function `prob_alternating(num_balls)` to calculate the probability that drawing all the balls one at a time will result in an alternating sequence of colors. Assume `num_balls` is even and greater than 0.
"""

import math

def prob_alternating(num_balls):
    num_white = num_balls // 2
    num_black = num_balls // 2
    return 2 * (math.factorial(num_white) * math.factorial(num_black)) / math.factorial(num_balls)