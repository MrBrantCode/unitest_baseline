"""
QUESTION:
Write a function named `calculate_critical_pressure` that takes in the molar mass, density, crystal structure, constant Kc, compressibility factor Zc, and cohesive energy E of a material as input parameters and returns the critical pressure of the material using the Gurney equation: Pc = Kc * (Zc / Vc) * (E / Vc)^(1/3). Assume that the critical pressure can only be calculated for materials with a face-centered cubic (fcc) crystal structure. If the crystal structure is not fcc, return `None` as the critical pressure.
"""

import math

def calculate_critical_pressure(molar_mass, density, crystal_structure, Kc, Zc, E):
    """
    Calculate the critical pressure of a material using the Gurney equation.

    Args:
        molar_mass (float): The molar mass of the material in g/mol.
        density (float): The density of the material in g/cm^3.
        crystal_structure (str): The crystal structure of the material.
        Kc (float): The constant Kc in the Gurney equation.
        Zc (float): The compressibility factor Zc in the Gurney equation.
        E (float): The cohesive energy E in the Gurney equation in kJ/mol.

    Returns:
        float or None: The critical pressure of the material in GPa, or None if the crystal structure is not fcc.
    """

    # Calculate the molar volume
    Vc = molar_mass / density

    # Check if the crystal structure is fcc
    if crystal_structure == 'fcc':
        # Calculate the critical pressure using the Gurney equation
        Pc = Kc * (Zc / Vc) * (E / Vc) ** (1/3)
        return Pc
    else:
        # Return None if the crystal structure is not fcc
        return None