"""
QUESTION:
Write a function `calculate_area` that takes the radius of a circle as input and returns its area. Implement an algorithm to approximate the value of pi without using the built-in `math` module or any other library.
"""

def calculate_area(radius):
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