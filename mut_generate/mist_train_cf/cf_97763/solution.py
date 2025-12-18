"""
QUESTION:
Design a function named `calculate_critical_pressure` that takes in the molar mass, density, and crystal structure of a material as input parameters and calculates the critical pressure using the Gurney equation. The function should return `None` if the crystal structure is not 'fcc'. The Gurney equation parameters are: Kc = 1.2, Zc = 0.3, and E = 100 kJ/mol.
"""

import math

def calculate_critical_pressure(molar_mass, density, crystal_structure):
    """
    Calculate the critical pressure using the Gurney equation.

    Args:
        molar_mass (float): The molar mass of the material in g/mol.
        density (float): The density of the material in g/cm^3.
        crystal_structure (str): The crystal structure of the material.

    Returns:
        float or None: The critical pressure in GPa if the crystal structure is 'fcc', otherwise None.
    """

    # Parameters for the Gurney equation
    Kc = 1.2
    Zc = 0.3
    E = 100  # in kJ/mol

    # Calculate the molar volume
    Vc = molar_mass / density

    # Calculate the critical pressure
    if crystal_structure == 'fcc':
        Pc = Kc * (Zc / Vc) * (E / Vc) ** (1/3)
        return Pc
    else:
        return None