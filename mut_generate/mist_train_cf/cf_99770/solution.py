"""
QUESTION:
Create a function `estimate_hydrocarbon_molecules` that calculates the total number of hydrocarbon molecules ingested by the fish each day given the mass of plankton consumed per day in grams and the concentration of hydrocarbons in water in parts per billion (ppb). The mass of one hydrocarbon molecule is 0.3 nanograms. The function should use Avogadro's number (6.02214076e23) for the calculation and return the total number of hydrocarbon molecules consumed per day.
"""

def estimate_hydrocarbon_molecules(plankton_mass, hydrocarbon_concentration):
    """
    Calculate the total number of hydrocarbon molecules ingested by the fish each day.

    Args:
    plankton_mass (float): Mass of plankton consumed per day in grams.
    hydrocarbon_concentration (float): Concentration of hydrocarbons in water in parts per billion (ppb).

    Returns:
    float: Total number of hydrocarbon molecules consumed per day.
    """
    AVOGADRO_NUMBER = 6.02214076e23  # Avogadro's number
    HYDROCARBON_MASS = 0.3e-21  # Mass of one hydrocarbon molecule in grams

    hydrocarbon_mass = plankton_mass * hydrocarbon_concentration  # Mass of hydrocarbons consumed per day in grams
    hydrocarbon_molecules = hydrocarbon_mass / HYDROCARBON_MASS  # Number of hydrocarbon molecules consumed per day
    total_molecules = hydrocarbon_molecules * AVOGADRO_NUMBER  # Total number of hydrocarbon molecules consumed per day

    return total_molecules