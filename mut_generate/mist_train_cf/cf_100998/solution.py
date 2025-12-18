"""
QUESTION:
Design a function `calculate_battery_lifespan` to calculate the lifespan of a battery in hours based on its chemical composition and operating conditions using the formula: `t = (A * exp(Ea / (R * T))) / I`. The function should take in the frequency factor `A`, the activation energy `Ea`, and the temperature `T` in Celsius as parameters. The gas constant `R` is 8.314 J/(mol*K) and the current density `I` is 0.1 A/cm^2. The function should convert the temperature from Celsius to Kelvin and return the calculated lifespan in hours.
"""

import math

def calculate_battery_lifespan(A, Ea, T):
    """
    Calculate the lifespan of a battery in hours based on its chemical composition and operating conditions.

    Parameters:
    A (float): Frequency factor
    Ea (float): Activation energy (J/mol)
    T (float): Temperature in Celsius

    Returns:
    float: Calculated lifespan in hours
    """
    R = 8.314  # Gas constant (J/(mol*K))
    I = 0.1    # Current density (A/cm^2)
    T_kelvin = T + 273.15  # Convert temperature to Kelvin
    t_seconds = (A * math.exp(Ea / (R * T_kelvin))) / I
    t_hours = t_seconds / 3600  # Convert seconds to hours
    return t_hours