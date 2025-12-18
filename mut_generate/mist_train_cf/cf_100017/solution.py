"""
QUESTION:
Design a function `calculate_critical_pressure` that calculates the critical pressure `Pc` of a material using the Gurney equation, which is given as `Pc = Kc * (Zc / Vc) * (E / Vc)^(1/3)`. The function should take in the following parameters: `Kc` (a constant that depends on the material), `Zc` (the compressibility factor), `E` (the cohesive energy), `molar_mass` (the molar mass of the material in g/mol), `density` (the density of the material in g/cm^3), and `crystal_structure` (the crystal structure of the material). The function should return the calculated critical pressure `Pc` in GPa if the crystal structure is 'fcc', and `None` otherwise.
"""

def calculate_critical_pressure(Kc, Zc, E, molar_mass, density, crystal_structure):
    """
    Calculate the critical pressure Pc of a material using the Gurney equation.

    Parameters:
    Kc (float): A constant that depends on the material.
    Zc (float): The compressibility factor.
    E (float): The cohesive energy in kJ/mol.
    molar_mass (float): The molar mass of the material in g/mol.
    density (float): The density of the material in g/cm^3.
    crystal_structure (str): The crystal structure of the material.

    Returns:
    float or None: The calculated critical pressure Pc in GPa if the crystal structure is 'fcc', and None otherwise.
    """
    Vc = molar_mass / density
    if crystal_structure == 'fcc':
        Pc = Kc * (Zc / Vc) * (E / Vc) ** (1/3)
        return Pc
    else:
        return None