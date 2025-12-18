"""
QUESTION:
Write a function `calculate_energy` that takes a mass `m` in kilograms as input and returns the energy produced in joules when the mass is converted into energy using Einstein's famous equation, E=mc^2. The speed of light `c` is approximately 299792458 meters per second.
"""

def calculate_energy(m):
    """
    Calculate the energy produced in joules when the mass is converted into energy using Einstein's famous equation, E=mc^2.

    Args:
        m (float): mass in kilograms

    Returns:
        float: energy in joules
    """
    c = 299792458  # speed of light in meters per second
    return m * c ** 2