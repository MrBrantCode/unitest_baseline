"""
QUESTION:
Write a function `calculate_critical_pressure` that takes in the molar mass, density, crystal structure, and cohesive energy of a material, and returns the critical pressure using the Gurney equation: `Pc = Kc * (Zc / Vc) * (E / Vc)^(1/3)`. Assume `Kc` is 1.2 and `Zc` is 0.3. The function should only return a critical pressure value for materials with a face-centered cubic (fcc) crystal structure, and return `None` otherwise. The molar mass is given in g/mol, the density is given in g/cm^3, and the cohesive energy is given in kJ/mol.
"""

def calculate_critical_pressure(molar_mass, density, crystal_structure, cohesive_energy):
    """
    Calculate the critical pressure of a material using the Gurney equation.

    Args:
        molar_mass (float): The molar mass of the material in g/mol.
        density (float): The density of the material in g/cm^3.
        crystal_structure (str): The crystal structure of the material.
        cohesive_energy (float): The cohesive energy of the material in kJ/mol.

    Returns:
        float or None: The critical pressure of the material in GPa if the crystal structure is fcc, otherwise None.
    """
    Kc = 1.2
    Zc = 0.3
    Vc = molar_mass / density
    if crystal_structure == 'fcc':
        return Kc * (Zc / Vc) * (cohesive_energy / Vc) ** (1/3)
    else:
        return None