"""
QUESTION:
Write a function named 'bulk_density' that calculates the bulk density of a polyhedron. The function should take two parameters: mass in grams and volume in cubic centimeters. The function should return the calculated bulk density in grams per cubic centimeter.
"""

def bulk_density(mass, volume):
    """
    Calculate the bulk density of a polyhedron.

    Parameters:
    mass (float): Mass in grams
    volume (float): Volume in cubic centimeters

    Returns:
    float: Bulk density in grams per cubic centimeter
    """
    return mass / volume