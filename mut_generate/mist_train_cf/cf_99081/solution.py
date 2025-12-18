"""
QUESTION:
Calculate the temperature of a lava flow given the heat flux, Stefan-Boltzmann constant, and emissivity. Create a function called `calculate_lava_temperature` that takes in three parameters: `heat_flux` in W/m^2, `stefan_boltzmann_constant` in W/(m^2*K^4), and `emissivity` as a unitless value. The function should return the calculated temperature in Kelvin, rounded to two decimal places. Assume the formula for temperature calculation is Temperature = Heat Flux / (Stefan-Boltzmann Constant x Emissivity)^(1/4).
"""

import math

def calculate_lava_temperature(heat_flux, stefan_boltzmann_constant, emissivity):
    """
    Calculate the temperature of a lava flow given the heat flux, Stefan-Boltzmann constant, and emissivity.

    Args:
        heat_flux (float): The heat flux in W/m^2.
        stefan_boltzmann_constant (float): The Stefan-Boltzmann constant in W/(m^2*K^4).
        emissivity (float): The emissivity as a unitless value.

    Returns:
        float: The calculated temperature in Kelvin, rounded to two decimal places.
    """
    temperature = heat_flux / (stefan_boltzmann_constant * emissivity)**(1/4)
    return round(temperature, 2)