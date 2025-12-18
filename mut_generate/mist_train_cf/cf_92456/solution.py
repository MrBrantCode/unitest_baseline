"""
QUESTION:
Create a Python class `ComplexNumber` with the following properties and methods:

- `__init__` method to initialize a complex number with real and imaginary parts.
- `add`, `subtract`, `multiply`, and `divide` methods to perform arithmetic operations on two complex numbers.
- `magnitude` method to calculate the magnitude of a complex number, rounded to two decimal places.
- `phase_angle` method to calculate the phase angle of a complex number in radians.
- A static method `cartesian_to_polar` to convert a complex number from Cartesian coordinates to polar coordinates, where the magnitude is rounded to two decimal places and the phase angle is returned in radians. 

The input for the `cartesian_to_polar` method should be two floats representing the real and imaginary parts of the complex number, and the output should be a tuple of two floats representing the magnitude and phase angle.
"""

import math

def cartesian_to_polar(real, imaginary):
    magnitude = math.sqrt(real**2 + imaginary**2)
    phase_angle = math.atan2(imaginary, real)
    return round(magnitude, 2), phase_angle