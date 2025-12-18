"""
QUESTION:
Implement a function `aNSeq` that takes three parameters: `Mbh` (mass of the black hole in kg), `Mns` (mass of the neutron star in kg), and `Pb` (orbital period of the binary system in seconds). The function should return the calculated semi-major axis of the binary system `aR` in meters and the semi-major axis of the neutron star orbiting the binary system `aNS` in meters, using the gravitational constant `G = 6.67430e-11 m^3 kg^-1 s^-2` and the formulas:
- `aR = (G * (Mbh + Mns) * (Pb^2) / (4 * pi^2))^(1/3)`
- `aNS = (Mbh / (Mbh + Mns)) * aR`
"""

from math import pi

# Gravitational constant
G = 6.67430e-11  # in m^3 kg^-1 s^-2

def aNSeq(Mbh, Mns, Pb):
    """
    Calculate the semi-major axis of the binary system (aR) and the semi-major axis of the neutron star orbiting the binary system (aNS).

    Args:
        Mbh (float): Mass of the black hole in kg.
        Mns (float): Mass of the neutron star in kg.
        Pb (float): Orbital period of the binary system in seconds.

    Returns:
        tuple: A tuple containing the semi-major axis of the binary system (aR) and the semi-major axis of the neutron star orbiting the binary system (aNS) in meters.
    """
    aR = ((G * (Mbh + Mns) * (Pb ** 2)) / (4 * (pi ** 2))) ** (1 / 3)
    aNS = (Mbh / (Mbh + Mns)) * aR
    return aR, aNS