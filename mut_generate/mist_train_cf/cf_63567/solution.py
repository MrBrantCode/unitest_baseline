"""
QUESTION:
Develop a function `compute_gravitational_force(mass1, mass2, distance)` that calculates the gravitational force between two celestial bodies given their masses (`mass1` and `mass2` in kilograms) and the average distance between them (`distance` in meters). Use the gravitational constant `G = 6.67430e-11` and the formula `F = G * (m1 * m2) / r^2`. Return the gravitational force in Newtons.
"""

def compute_gravitational_force(mass1, mass2, distance):
    # Gravitational constant
    G = 6.67430e-11 

    # Calculate the gravitational force
    force = G * (mass1 * mass2) / (distance ** 2)
    
    return force