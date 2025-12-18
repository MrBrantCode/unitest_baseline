"""
QUESTION:
Write a function `calculate_grav_pull` that calculates the gravitational pull of Earth on an object with given mass at a certain height above the Earth's surface. The function should take an array of pairs as input where each pair contains the mass of the object and its height above the Earth's surface. The function should return an array of gravitational forces for each object, with a force of 0 for objects below ground level (negative height) or above the exosphere (height above 100,000m). Use the formula `F = G * (m1*m2)/(r^2)` for the calculation, where G is the gravitational constant, m1 is the mass of the object, m2 is the mass of the Earth, and r is the distance from the object to the center of the Earth. Assume the mass of the Earth is 5.972 × 10^24 kg and the radius of the Earth is 6.371 × 10^6 m.
"""

import math

G = 6.67430 * math.pow(10, -11) # m3 kg^-1 s^-2
ME = 5.972 * math.pow(10, 24) # kg
RE = 6.371 * math.pow(10, 6) # m
EXOSPHERE = 100000 # m

def calculate_grav_pull(mass_height):
    grav_force = []
    
    for obj in mass_height:
        mass = obj[0]
        height = obj[1]

        # check if height is below ground level or beyond earth's atmospheric limit
        if (height < 0 or height > EXOSPHERE):
            grav_force.append(0)
        else:
            r = RE + height
            F = G * (mass * ME) / math.pow(r, 2)
            grav_force.append(F)
    
    return grav_force