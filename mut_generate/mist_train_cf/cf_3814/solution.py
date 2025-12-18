"""
QUESTION:
Write a function named `calculate_sphere_volume` that calculates the volume of a sphere using the formula V = 4 * π * r^3, where V is the volume and r is the radius of the sphere. Do not use any mathematical libraries or built-in functions for calculating the volume of a sphere. The function should take the radius of the sphere as input and return the calculated volume.
"""

def calculate_sphere_volume(radius):
    """
    Calculate the volume of a sphere using the formula V = 4 * π * r^3.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The calculated volume of the sphere.
    """
    pi = 3.14159  # Approximate value of pi
    return 4 * pi * radius ** 3