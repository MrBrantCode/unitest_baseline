"""
QUESTION:
Write a function called `calculate_critical_pressure` that calculates the critical pressure (Pc) of a material using the Gurney equation, given the material's molar mass, density, crystal structure, and cohesive energy. The function should take four parameters: `molar_mass` (in g/mol), `density` (in g/cm^3), `crystal_structure`, and `cohesive_energy` (in kJ/mol). It should return the calculated critical pressure in GPa if the crystal structure is 'fcc', otherwise return None. Assume the value of Kc is 1.2 and Zc is 0.3.
"""

def calculate_critical_pressure(molar_mass, density, crystal_structure, cohesive_energy):
    """
    Calculate the critical pressure of a material using the Gurney equation.

    Parameters:
    molar_mass (float): The molar mass of the material in g/mol.
    density (float): The density of the material in g/cm^3.
    crystal_structure (str): The crystal structure of the material.
    cohesive_energy (float): The cohesive energy of the material in kJ/mol.

    Returns:
    float or None: The calculated critical pressure in GPa if the crystal structure is 'fcc', otherwise None.
    """
    Kc = 1.2
    Zc = 0.3
    Vc = molar_mass / density
    if crystal_structure == 'fcc':
        Pc = Kc * (Zc / Vc) * (cohesive_energy / Vc) ** (1/3)
        return Pc
    else:
        return None