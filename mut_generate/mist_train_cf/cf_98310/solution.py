"""
QUESTION:
Write a recursive function `calculate_gravitational_force` that takes in two or more masses and their respective distances, as well as optional unit parameters for mass and distance. The function should calculate and return the total gravitational force between the objects using the formula F = G * (m1 * m2) / r^2, where G is the gravitational constant (6.6743e-11 m^3/(kg*s^2)). The function should also handle unit conversions for mass (kg, g, lb) and distance (m, km, mi). If only two masses and one distance are provided, the function should return the gravitational force between those two objects. If more than two masses and their respective distances are provided, the function should recursively calculate the total gravitational force between all objects.
"""

G = 6.6743e-11 # gravitational constant in m^3/(kg*s^2)
def calculate_gravitational_force(masses, distances, m_unit='kg', d_unit='m'):
    mass_converter = {'kg': 1, 'g': 1e-3, 'lb': 0.453592}
    distance_converter = {'m': 1, 'km': 1000, 'mi': 1609.34}
    if len(masses) == 2:
        m1, m2 = masses
        r = distances[0] * distance_converter[d_unit]
        m1_kg = m1 * mass_converter[m_unit]
        m2_kg = m2 * mass_converter[m_unit]
        force = G * m1_kg * m2_kg / r**2
        return force
    else:
        m1 = masses[0]
        d1 = distances[0]
        m2 = calculate_gravitational_force(masses[1:], distances[1:], m_unit, d_unit)
        r = d1 * distance_converter[d_unit]
        m1_kg = m1 * mass_converter[m_unit]
        m2_kg = m2 * mass_converter['kg']
        force = G * m1_kg * m2_kg / r**2
        return force