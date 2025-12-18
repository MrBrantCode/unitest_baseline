"""
QUESTION:
Write a function `simulate_fall` that simulates a stone being dropped from various initial velocities in different gravitational fields, and calculate the time it takes for the stone to fall and the distance it covers. 

The function should take two parameters: `initial_velocity` (in m/s) and `gravity_force` (in m/s^2). It should return the time it takes for the stone to fall and the distance it covers. 

Assume negligible air resistance. Use the following formula to calculate the time and distance: t = initial_velocity / gravity_force and y = 0.5*gravity_force*(t**2). 

Test the function with initial velocities ranging from 30m/s to 100m/s with a 10m/s increment, and gravitational forces for the Earth, Moon, and Mars.
"""

import numpy as np

# gravity constants for different planets in m/s^2
gravity = {
    "earth": 9.81,
    "moon": 1.622,
    "mars": 3.72076
}

def simulate_fall(initial_velocity, gravity_force):
    # using simple physics formula
    t = initial_velocity / gravity_force
    y = 0.5*gravity_force*(t**2)

    return t, y