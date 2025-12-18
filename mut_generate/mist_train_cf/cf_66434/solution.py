"""
QUESTION:
Write a function named `model` that takes two parameters: `populations` (a list of two elements representing the rabbit and fox populations) and `t` (time). The function should return a list of the derivatives of rabbit and fox populations with respect to time. The derivatives should be calculated using the Lotka-Volterra equations: `drdt = r * rabbit - b * rabbit * fox` and `dfdt = c * rabbit * fox - a * fox`, where `r`, `a`, `b`, and `c` are given parameters representing the rates of growth and decline for rabbits and foxes.
"""

import numpy as np

# function that returns dy/dt
def model(populations, t, r, a, b, c):
    rabbit, fox = populations
    drdt = r * rabbit - b * rabbit * fox
    dfdt = c * rabbit * fox - a * fox
    return [drdt, dfdt]