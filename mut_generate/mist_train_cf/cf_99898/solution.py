"""
QUESTION:
Write a function called `calculate_battery_lifespan` that takes as input the frequency factor `A`, activation energy `Ea`, gas constant `R`, temperature in Celsius `T`, and current density `I`, and returns the calculated lifespan in hours using the formula t = (A * exp(Ea / (R * T))) / I, where T is converted to Kelvin. The function should not take any arguments with default values.
"""

import math

def calculate_battery_lifespan(A, Ea, R, T, I):
    """
    Calculate the lifespan of a battery based on the given formula.

    Parameters:
    A (float): Frequency factor
    Ea (float): Activation energy (J/mol)
    R (float): Gas constant (J/(mol*K))
    T (float): Temperature in Celsius
    I (float): Current density (A/cm^2)

    Returns:
    float: Calculated lifespan in hours
    """
    T_kelvin = T + 273.15  # Convert temperature to Kelvin
    lifespan = (A * math.exp(Ea / (R * T_kelvin))) / I
    return lifespan / 3600  # Convert to hours