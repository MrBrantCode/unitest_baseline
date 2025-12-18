"""
QUESTION:
Write a function `gravitational_force` that computes the gravitational force between two masses using the formula F = G * ((m1 * m2) / r^2), where G is the gravitational constant (6.67430 x 10^-11 N*m^2/kg^2), m1 and m2 are the masses in kilograms, and r is the distance between the centers of the masses in meters. The function should take m1, m2, and r as input parameters and return the gravitational force in Newtons.
"""

def gravitational_force(m1, m2, r):
    """
    Compute the gravitational force between two masses.

    Parameters:
    m1 (float): Mass of object 1 in kg
    m2 (float): Mass of object 2 in kg
    r (float): Distance between the centers of the masses in meters

    Returns:
    float: Gravitational force in Newtons
    """
    G = 6.67430e-11  # Gravitational constant
    return G * ((m1 * m2) / (r**2))