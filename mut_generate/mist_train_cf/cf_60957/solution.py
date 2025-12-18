"""
QUESTION:
Create a function `calculate_gravitational_force(body, altitude, object_mass)` that calculates the gravitational force on an object of `object_mass` kilograms at a given `altitude` above the surface of a specified celestial body (`body`). The function should use the formula F = G * ((m1 * m2) / r^2), where G is the gravitational constant (6.674 * 10^-11 m^3 kg^-1 s^-2), `m1` is the mass of the celestial body, `m2` is the mass of the object, and `r` is the distance between the center of the celestial body and the object. The function should support calculations for the following celestial bodies: Earth, Moon, Mars, Jupiter, and Venus. The radii and masses of these celestial bodies should be hard-coded in the function. The function should return the gravitational force in Newtons.
"""

import math

# Gravitational constant in m^3 kg^-1 s^-2
G = 6.674 * math.pow(10, -11)

# Radii and masses of celestial bodies in meters and kilograms respectively
celestial_bodies = {
    "Earth": {"radius": 6.371 * math.pow(10, 6), "mass": 5.972 * math.pow(10, 24)},
    "Moon": {"radius": 1.737 * math.pow(10, 6), "mass": 7.348 * math.pow(10, 22)},
    "Mars": {"radius": 3.390 * math.pow(10, 6), "mass": 6.417 * math.pow(10, 23)},
    "Jupiter": {"radius": 6.9911 * math.pow(10, 7), "mass": 1.898 * math.pow(10, 27)},
    "Venus": {"radius": 6.0518 * math.pow(10, 6), "mass": 4.867 * math.pow(10, 24)}
}

def calculate_gravitational_force(body, altitude, object_mass):
    """
    Calculate the gravitational force on an object of object_mass kilograms at a given altitude above the surface of a specified celestial body.
    
    Args:
        body (str): The name of the celestial body.
        altitude (float): The altitude above the celestial body's surface in meters.
        object_mass (float): The mass of the object in kilograms.
    
    Returns:
        float: The gravitational force in Newtons.
    """
    r_meters = celestial_bodies[body]["radius"] + altitude
    m = celestial_bodies[body]["mass"]
    F = G * (m * object_mass) / math.pow(r_meters, 2)
    return F