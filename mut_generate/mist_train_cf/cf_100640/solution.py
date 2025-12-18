"""
QUESTION:
Write a function `estimate_hydrocarbon_molecules` that calculates the total number of hydrocarbon molecules ingested by a fish per day. The function should take two arguments: `plankton_mass` in grams and `hydrocarbon_concentration` in parts per billion (ppb). The mass of one hydrocarbon molecule is 0.3 nanograms (or 0.3e-21 grams) and Avogadro's number is 6.02214076e23.
"""

def estimate_hydrocarbon_molecules(plankton_mass, hydrocarbon_concentration):
    """
    Calculate the total number of hydrocarbon molecules ingested by a fish per day.

    Args:
    plankton_mass (float): Mass of plankton consumed per day in grams.
    hydrocarbon_concentration (float): Concentration of hydrocarbons in water in parts per billion (ppb).

    Returns:
    float: Total number of hydrocarbon molecules ingested by the fish per day.
    """
    AVOGADRO_NUMBER = 6.02214076e23  # Avogadro's number
    HYDROCARBON_MASS = 0.3e-21  # Mass of one hydrocarbon molecule in grams
    hydrocarbon_mass = plankton_mass * hydrocarbon_concentration  # Mass of hydrocarbons consumed per day in grams
    hydrocarbon_molecules = hydrocarbon_mass / HYDROCARBON_MASS  # Number of hydrocarbon molecules consumed per day
    total_molecules = hydrocarbon_molecules * AVOGADRO_NUMBER  # Total number of hydrocarbon molecules consumed per day
    return total_molecules