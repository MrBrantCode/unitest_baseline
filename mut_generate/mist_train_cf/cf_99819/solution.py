"""
QUESTION:
Design a function `calculate_critical_pressure` that takes in `Kc`, `Zc`, `E`, `molar_mass`, `density`, and `crystal_structure` as parameters and returns the critical pressure `Pc` of a material using the Gurney equation `Pc = Kc * (Zc / Vc) * (E / Vc)^(1/3)` where `Vc` is the molar volume calculated as `molar_mass / density`. The function should only return a value for materials with an 'fcc' crystal structure, otherwise it should return `None`. The input units are `Kc` (unitless), `Zc` (unitless), `E` (kJ/mol), `molar_mass` (g/mol), and `density` (g/cm^3), and the output unit is GPa.
"""

import math

def calculate_critical_pressure(Kc, Zc, E, molar_mass, density, crystal_structure):
    """
    Calculate the critical pressure of a material using the Gurney equation.

    Args:
    Kc (float): A constant that depends on the material (unitless).
    Zc (float): The compressibility factor (unitless).
    E (float): The cohesive energy (kJ/mol).
    molar_mass (float): The molar mass of the material (g/mol).
    density (float): The density of the material (g/cm^3).
    crystal_structure (str): The crystal structure of the material.

    Returns:
    float or None: The critical pressure of the material (GPa) if the crystal structure is 'fcc', otherwise None.
    """
    if crystal_structure != 'fcc':
        return None

    # Calculate the molar volume
    Vc = molar_mass / density

    # Calculate the critical pressure
    Pc = Kc * (Zc / Vc) * (E / Vc) ** (1/3)
    
    return Pc