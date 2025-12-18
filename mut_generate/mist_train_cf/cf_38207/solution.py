"""
QUESTION:
Write a function `calculate_gravitational_force(x_dist, y_dist)` that takes two integers `x_dist` and `y_dist` as input, representing the x and y distances between a planet and an object. The function should calculate the pre-calculated gravitational force using the formula `force = 2^21 / (x_dist^2 + y_dist^2)^(3/2)`, and return the result as a 21-bit binary number. If `x_dist` and `y_dist` are both zero, the function should return an error message.
"""

def entrance(x_dist, y_dist):
    if x_dist == 0 and y_dist == 0:
        return "Invalid input: x_dist and y_dist cannot both be zero"
    else:
        force = int((2**21) / (x_dist**2 + y_dist**2)**(3/2))
        return format(force, '021b')