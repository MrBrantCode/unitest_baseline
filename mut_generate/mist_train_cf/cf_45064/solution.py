"""
QUESTION:
Create a function named `gravitational_force` that calculates the gravitational force between two celestial bodies. The function should take three parameters: the masses of the two bodies (`mass1` and `mass2`) and the distance between them. The gravitational constant is 6.674 * 10^-11. The function should return the calculated gravitational force.
"""

def gravitational_force(mass1, mass2, distance):
    """
    Calculate the gravitational force between two celestial bodies.

    Args:
    mass1 (float): Mass of the first celestial body in kg.
    mass2 (float): Mass of the second celestial body in kg.
    distance (float): Distance between the two celestial bodies in meters.

    Returns:
    float: The gravitational force between the two celestial bodies in Newtons.
    """
    gravitational_constant = 6.674 * (10 ** -11)
    force = gravitational_constant * (mass1 * mass2) / (distance ** 2)
    return force