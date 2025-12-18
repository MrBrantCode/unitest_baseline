"""
QUESTION:
Write a function `calculate_hydrocarbon_molecules` that estimates the total number of hydrocarbon molecules ingested by a fish each day. The function takes as input the mass of plankton consumed per day in grams and the concentration of hydrocarbons in water in parts per billion (ppb), and uses the given constants for Avogadro's number and the mass of one hydrocarbon molecule in grams. The function returns the total number of hydrocarbon molecules consumed per day.
"""

def calculate_hydrocarbon_molecules(plankton_mass, hydrocarbon_concentration):
    """
    Estimates the total number of hydrocarbon molecules ingested by a fish each day.
    
    Args:
    plankton_mass (float): Mass of plankton consumed per day in grams
    hydrocarbon_concentration (float): Concentration of hydrocarbons in water in parts per billion (ppb)
    
    Returns:
    float: Total number of hydrocarbon molecules consumed per day
    """
    AVOGADRO_NUMBER = 6.02214076e23  # Avogadro's number
    HYDROCARBON_MASS = 0.3e-21  # Mass of one hydrocarbon molecule in grams
    
    hydrocarbon_mass = plankton_mass * hydrocarbon_concentration
    hydrocarbon_molecules = hydrocarbon_mass / HYDROCARBON_MASS
    total_molecules = hydrocarbon_molecules * AVOGADRO_NUMBER
    
    return total_molecules