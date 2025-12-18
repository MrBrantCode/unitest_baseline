"""
QUESTION:
Write a function named `volume_of_parallelepiped` that calculates the volume of a rectangular parallelepiped given its length, width, and height. The function should take three parameters: length, width, and height, all of which are expected to be positive numbers. If any of the input dimensions are negative, the function should return an error message instead of a volume.
"""

def volume_of_parallelepiped(length, width, height):
    if length < 0 or width < 0 or height < 0:
        return "Invalid input! Dimension(s) should be positive."
    return length * width * height