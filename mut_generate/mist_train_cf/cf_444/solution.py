"""
QUESTION:
Write a function `calculate_area(radius)` to calculate the area of a circle given its radius. You cannot use the built-in `math` module or any other library that provides a method for calculating the value of pi. Implement your own algorithm to approximate the value of pi.
"""

def entance(radius):
    # Approximating the value of pi using Leibniz formula for pi/4
    num_iterations = 100000
    pi_approximation = 0
    sign = 1
    for i in range(0, num_iterations):
        term = sign / (2 * i + 1)
        pi_approximation += term
        sign *= -1

    # Multiplying pi approximation by 4 to get a better estimate
    pi_approximation *= 4

    # Calculating the area of the circle
    area = pi_approximation * (radius ** 2)
    return area