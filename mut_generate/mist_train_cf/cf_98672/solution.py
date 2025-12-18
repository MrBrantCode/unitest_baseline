"""
QUESTION:
Design a function `calculate_battery_lifespan` that takes in the frequency factor `A`, activation energy `Ea`, and the operating temperature in Celsius `T_celsius` and current density `I`, and returns the predicted lifespan of the battery in hours. Use the formula `t = (A * exp(Ea / (R * T))) / I`, where `R` is the gas constant (8.314 J/(mol*K)) and `T` is the temperature in Kelvin. Assume `R` is already defined as 8.314. The function should convert the temperature from Celsius to Kelvin before performing the calculation.
"""

import math

def calculate_battery_lifespan(A, Ea, T_celsius, I):
    """
    Calculate the predicted lifespan of the battery in hours.

    Parameters:
    A (float): Frequency factor
    Ea (float): Activation energy in J/mol
    T_celsius (float): Operating temperature in Celsius
    I (float): Current density in A/cm^2

    Returns:
    float: Predicted lifespan of the battery in hours
    """
    R = 8.314  # Gas constant (J/(mol*K))
    T = T_celsius + 273.15  # Temperature in Kelvin
    t = (A * math.exp(Ea / (R * T))) / I  # Calculate lifespan in seconds
    return t / 3600  # Convert to hours