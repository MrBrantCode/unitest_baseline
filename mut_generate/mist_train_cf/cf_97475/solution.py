"""
QUESTION:
Develop a function named calculate_circumference that takes a string input representing the radius of a circle, extracts the numerical value, validates it as a positive number, and returns the circumference of the circle as a floating-point number. The input string may contain additional characters, and the function should handle radius inputs in different units. If the input is invalid, the function should return an error message.
"""

import math

def calculate_circumference(radius):
    # Remove any additional characters from the radius string
    radius = ''.join(filter(str.isdigit, radius))

    # Validate the input to ensure that the radius is a positive number
    if not radius or not radius.isdigit() or float(radius) <= 0:
        return "Error: Invalid radius input"

    # Convert the numerical value of the radius to a float
    radius = float(radius)

    # Calculate the circumference
    circumference = 2 * math.pi * radius

    return circumference