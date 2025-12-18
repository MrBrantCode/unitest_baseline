"""
QUESTION:
Design a function named `calculate_battery_lifespan` that calculates the lifespan of a battery in hours based on its chemical composition and operating conditions. The function should take the frequency factor `A` (1/s), the activation energy `Ea` (J/mol), and the current density `I` (A/cm^2) as input parameters. It should use the formula `t = (A * exp(Ea / (R * T))) / I`, where `R` is the gas constant (8.314 J/(mol*K)) and `T` is the temperature in Kelvin. Assume a constant temperature of 60 degrees Celsius (333.15 K).
"""

import math

def calculate_battery_lifespan(A, Ea, I):
    """
    Calculate the lifespan of a battery in hours.

    Parameters:
    A (float): Frequency factor (1/s)
    Ea (float): Activation energy (J/mol)
    I (float): Current density (A/cm^2)

    Returns:
    float: Lifespan of the battery in hours
    """
    R = 8.314  # Gas constant (J/(mol*K))
    T = 60 + 273.15  # Temperature in Kelvin (constant)
    t = (A * math.exp(Ea / (R * T))) / I
    return t / 3600  # Convert to hours