"""
QUESTION:
Implement a function named `calculate_magnetic_field` that calculates the magnetic field components (Ex, Ey, Ez) at specified locations and times given the magnetic susceptibility (kappa) and relative permittivity (epsr) values. The function should take kappa and epsr as input parameters, use the formula mu = mu_0 * (1 + kappa) to calculate the magnetic field components, and return them as numpy arrays. The function should have the following signature: 
def calculate_magnetic_field(kappa=0.0, epsr=1.0):
"""

import numpy as np

def calculate_magnetic_field(kappa=0.0, epsr=1.0):
    # Constants
    mu_0 = 4 * np.pi * 10**-7  # Permeability of free space

    # Calculate mu using the provided formula
    mu = mu_0 * (1 + kappa)

    # Calculate the magnetic field components (Ex, Ey, Ez) using the given values
    # Replace the following lines with the actual calculations based on the specified locations and times
    Ex = np.array([1, 2, 3])  # Replace with actual calculations
    Ey = np.array([4, 5, 6])  # Replace with actual calculations
    Ez = np.array([7, 8, 9])  # Replace with actual calculations

    return Ex, Ey, Ez