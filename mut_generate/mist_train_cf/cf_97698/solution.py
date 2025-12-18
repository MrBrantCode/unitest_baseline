"""
QUESTION:
Design a function called `calculate_critical_pressure` that takes the molar mass, density, and crystal structure of a material as input parameters and returns the critical pressure of the material using the Gurney equation. The function should only work for materials with a face-centered cubic (fcc) crystal structure. If the crystal structure is not fcc, the function should return `None`. The Gurney equation parameters are: Kc = 1.2, Zc = 0.3, E = 100 kJ/mol. The molar mass is in g/mol and the density is in g/cm^3. The critical pressure should be returned in GPa.
"""

def calculate_critical_pressure(molar_mass, density, crystal_structure):
    """
    Calculate the critical pressure of a material using the Gurney equation.
    
    Parameters:
    molar_mass (float): The molar mass of the material in g/mol.
    density (float): The density of the material in g/cm^3.
    crystal_structure (str): The crystal structure of the material. Only 'fcc' is supported.
    
    Returns:
    float or None: The critical pressure of the material in GPa, or None if the crystal structure is not 'fcc'.
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
    else:
        Pc = None
        
    return Pc