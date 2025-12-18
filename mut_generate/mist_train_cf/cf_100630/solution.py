"""
QUESTION:
Create a function `calculate_gravitational_force` to calculate the gravitational force between two or more objects. The function should take in the masses of the objects and the distance between them, and return the gravitational force. The function should also be able to handle different units of mass and distance. If multiple objects are provided, the function should calculate the total gravitational force between all objects. 

The function should take in the following parameters: 
- `masses`: a list of masses of the objects. If only two objects are provided, the masses can be passed in as two separate arguments.
- `distances`: a list of distances between the objects.
- `m_unit`: the unit of the masses (default is 'kg').
- `d_unit`: the unit of the distances (default is 'm').

The function should return the total gravitational force between the objects. The gravitational constant G is 6.6743e-11 m^3/(kg*s^2).
"""

G = 6.6743e-11 # gravitational constant in m^3/(kg*s^2)

def calculate_gravitational_force(masses, distances, m_unit='kg', d_unit='m'):
    mass_converter = {'kg': 1, 'g': 1e-3, 'lb': 0.453592}
    distance_converter = {'m': 1, 'km': 1000, 'mi': 1609.34}
    total_force = 0
    for i in range(len(masses)):
        for j in range(i + 1, len(masses)):
            m1_kg = masses[i] * mass_converter[m_unit]
            m2_kg = masses[j] * mass_converter[m_unit]
            r_m = distances[j - 1] * distance_converter[d_unit]
            force = G * m1_kg * m2_kg / r_m**2
            total_force += force
    return total_force