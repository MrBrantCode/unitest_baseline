"""
QUESTION:
Create a function `calculate_max_RPM(diameter)` that calculates the maximum revolutions per minute (RPM) for a given propeller diameter, ensuring the tip speed does not exceed 0.7 times the speed of sound at sea level. Assume standard sea level conditions: adiabatic index of 1.4, specific gas constant for dry air of 287 J/(kg·K), temperature of 288.15 K, and π as 3.14159. The function should take the propeller diameter as input and return the maximum RPM.
"""

import math

def calculate_max_RPM(diameter):
    gamma = 1.4  # adiabatic index for air
    R = 287  # specific gas constant for dry air in J/(kg·K)
    T = 288.15  # standard sea level temperature in Kelvin
    speed_of_sound = math.sqrt(gamma * R * T)  # calculate speed of sound

    max_RPM = (0.7 * speed_of_sound * 60) / (math.pi * diameter)  # calculate max RPM
    return max_RPM