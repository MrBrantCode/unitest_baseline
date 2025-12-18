"""
QUESTION:
Write a function `calculate_battery_lifespan` that calculates the lifespan of a battery in hours based on its chemical composition and operating conditions. The lifespan is calculated using the formula `t = (A * exp(Ea / (R * T))) / I`, where `A` represents the frequency factor, `Ea` represents the activation energy, `R` represents the gas constant, `T` represents the temperature in Kelvin, and `I` represents the current density. The function should take the parameters `A`, `Ea`, `T`, and `I` as input and return the calculated lifespan in hours. The gas constant `R` is 8.314 J/(mol*K) and should be assumed as a constant within the function.
"""

import math

def calculate_battery_lifespan(A, Ea, T, I):
    """
    Calculate the lifespan of a battery in hours based on its chemical composition and operating conditions.

    Parameters:
    A (float): Frequency factor
    Ea (float): Activation energy (J/mol)
    T (float): Temperature in Kelvin
    I (float): Current density (A/cm^2)

    Returns:
    float: Calculated lifespan in hours
    """
    R = 8.314  # Gas constant (J/(mol*K))
    t = (A * math.exp(Ea / (R * T))) / I
    return t / 3600  # Convert to hours