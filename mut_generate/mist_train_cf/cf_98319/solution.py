"""
QUESTION:
Develop a function `calculate_hydrocarbon_molecules` that estimates the total number of hydrocarbon molecules ingested by the fish each day. The function should take three parameters: `plankton_mass` (the mass of plankton consumed per day in grams), `hydrocarbon_concentration` (the concentration of hydrocarbons in water in parts per billion), and `hydrocarbon_size` (the average size of a hydrocarbon molecule in nanometers). The function should use Avogadro's number (approximately 6.02214076e23) and return the total number of hydrocarbon molecules consumed per day. Assume the molar mass of a hydrocarbon molecule is 12 g/mol (one carbon atom per molecule) and 1 nanometer is equal to 10^-7 grams.
"""

def calculate_hydrocarbon_molecules(plankton_mass, hydrocarbon_concentration, hydrocarbon_size):
    """
    Estimates the total number of hydrocarbon molecules ingested by the fish each day.

    Parameters:
    plankton_mass (float): Mass of plankton consumed per day in grams.
    hydrocarbon_concentration (float): Concentration of hydrocarbons in water in parts per billion.
    hydrocarbon_size (float): Average size of a hydrocarbon molecule in nanometers.

    Returns:
    float: Total number of hydrocarbon molecules consumed per day.
    """
    AVOGADRO_NUMBER = 6.02214076e23  # Avogadro's number
    HYDROCARBON_MASS = 12  # Molar mass of a hydrocarbon molecule in g/mol
    hydrocarbon_mass = (plankton_mass * hydrocarbon_concentration * 1e-9) / (1e-6 * HYDROCARBON_MASS) 
    hydrocarbon_molecules = (hydrocarbon_mass / HYDROCARBON_MASS) * AVOGADRO_NUMBER
    return hydrocarbon_molecules