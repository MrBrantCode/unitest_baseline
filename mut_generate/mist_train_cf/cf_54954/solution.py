"""
QUESTION:
Write a function named `compute_gravitational_force` that takes four parameters: two masses `m1` and `m2` in kilograms, and their respective elevations `e1` and `e2` from the earth's surface in meters. The function should calculate and return the adjusted gravitational force between the two masses considering the variation in the gravitational constant based on the elevation of the masses from the surface of the earth. The function should use the gravitational constant `G = 6.674 * (10 ** -11)` and the radius of the earth `r = 6371 km`.
"""

def compute_gravitational_force(m1, m2, e1, e2):
    # Given values:
    # gravitational constant (G) = 6.674 * (10 ** -11)
    # radius of the Earth (r) = 6371 km
    
    G = 6.674 * (10 ** -11) 
    r = 6371 * 10**3  # Converted to meters

    G_surface = G / (r ** 2)
    G_e1 = G_surface * (r / (r + e1))**2
    G_e2 = G_surface * (r / (r + e2))**2

    F_e1 = G_e1 * ((m1 * m2) / (r ** 2))
    F_e2 = G_e2 * ((m1 * m2) / (r ** 2))

    adjusted_gravitational_force = (F_e1 + F_e2) / 2

    return adjusted_gravitational_force