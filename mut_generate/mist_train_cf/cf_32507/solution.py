"""
QUESTION:
Implement the function `calculate_virial_radius` that calculates the virial radius of a dark matter halo given the concentration, halo mass, and overdensity with respect to the mean matter density. The function should take four parameters: `concentration` (float), `halo_mass` (float), `odelta` (float), and `critical_density` (float), and return the calculated virial radius. Use the formula Rvir = (3 * halo_mass / (4 * pi * odelta * critical_density * concentration^3))^(1/3).
"""

import math

def calculate_virial_radius(concentration, halo_mass, odelta, critical_density):
    pi = math.pi
    virial_radius = (3 * halo_mass / (4 * pi * odelta * critical_density * concentration**3))**(1/3)
    return virial_radius