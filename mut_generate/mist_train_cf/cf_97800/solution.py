"""
QUESTION:
Write a function named `calculate_energy` that takes a mass in kilograms as input and returns the energy produced when this mass is converted into energy using Einstein's famous equation, E=mc^2. The speed of light is approximately 299,792,458 meters per second.
"""

def calculate_energy(m):
    """
    Calculate the energy produced when a mass is converted into energy using Einstein's famous equation, E=mc^2.

    Args:
    m (float): The mass in kilograms.

    Returns:
    float: The energy produced in joules.
    """
    c = 299792458  # speed of light in meters per second
    return m * c**2