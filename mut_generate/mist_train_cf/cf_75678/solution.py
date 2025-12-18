"""
QUESTION:
Develop a function `gravitational_force(m, h)` that calculates the gravitational force exerted by Earth on an object of mass `m` kilograms situated at an altitude of `h` meters above the Earth's surface. The function should use the gravitational constant (G = 6.674 * 10^-11), the mass of the Earth (M = 5.972 * 10^24 kg), and the radius of the Earth (R = 6371000 meters). The gravitational force formula is F = G * ((M * m) / r^2), where r is the distance from the center of the Earth (r = R + h).
"""

import math

def gravitational_force(m, h):
    # constants
    G = 6.674 * (10**-11) # gravitational constant
    M = 5.972 * (10**24) # mass of the earth
    R = 6371000 # radius of the earth in meters

    # Gravitational force formula:
    # F = G * ((m1 * m2) / r^2)
    r = R + h # the distance from the center of the earth
    F = G * ((M * m) / r**2)
    
    return F