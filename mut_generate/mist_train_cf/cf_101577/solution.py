"""
QUESTION:
Design a function named `calculate_battery_lifespan` that takes frequency factor `A`, activation energy `Ea`, temperature in Celsius `T`, and current density `I` as inputs. The function should use the formula `t = (A * exp(Ea / (R * T))) / I` to calculate the lifespan of a battery in hours, where `R` is the gas constant (8.314 J/(mol*K)) and temperature `T` is converted to Kelvin. The function should return the calculated lifespan in hours. The inputs are: `A = 2E9`, `Ea = 20,000 J/mol`, `T = 60 degrees Celsius`, and `I = 0.1 A/cm^2`.
"""

import math

def calculate_battery_lifespan(A, Ea, T, I):
    """
    Calculate the lifespan of a battery in hours.
    
    Parameters:
    A (float): Frequency factor
    Ea (float): Activation energy (J/mol)
    T (float): Temperature in Celsius
    I (float): Current density (A/cm^2)
    
    Returns:
    float: The calculated lifespan of the battery in hours
    """
    R = 8.314  # Gas constant (J/(mol*K))
    T_kelvin = T + 273.15  # Convert temperature to Kelvin
    t = (A * math.exp(Ea / (R * T_kelvin))) / I
    return t / 3600  # Convert to hours