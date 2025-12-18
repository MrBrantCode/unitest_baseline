"""
QUESTION:
Write a function `calculate_hydrocarbon_molecules` that estimates the total number of hydrocarbon molecules ingested by the fish each day. The function should take three parameters: `plankton_mass` (the mass of plankton consumed per day in grams), `hydrocarbon_concentration` (the concentration of hydrocarbons in water in parts per billion), and `hydrocarbon_size` (the size of one hydrocarbon molecule in nanometers). The function should use Avogadro's number (6.02214076e23) and return the total number of hydrocarbon molecules ingested by the fish each day.
"""

AVOGADRO_NUMBER = 6.02214076e23  # Avogadro's number
HYDROCARBON_MASS = 0.3e-21  # Mass of one hydrocarbon molecule in grams

def calculate_hydrocarbon_molecules(plankton_mass, hydrocarbon_concentration, hydrocarbon_size):
    """
    Estimates the total number of hydrocarbon molecules ingested by the fish each day.

    Parameters:
    plankton_mass (float): Mass of plankton consumed per day in grams
    hydrocarbon_concentration (float): Concentration of hydrocarbons in water in parts per billion
    hydrocarbon_size (float): Size of one hydrocarbon molecule in nanometers

    Returns:
    float: Total number of hydrocarbon molecules ingested by the fish each day
    """
    hydrocarbon_mass = plankton_mass * hydrocarbon_concentration
    hydrocarbon_molecules = hydrocarbon_mass / HYDROCARBON_MASS
    total_molecules = hydrocarbon_molecules * AVOGADRO_NUMBER
    return total_molecules