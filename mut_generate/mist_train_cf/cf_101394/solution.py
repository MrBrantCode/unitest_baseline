"""
QUESTION:
Write a Python function `calculate_lava_temperature` that calculates the temperature of a lava flow given heat flux, Stefan-Boltzmann Constant, and emissivity. The formula for the calculation is Temperature = Heat Flux / (Stefan-Boltzmann Constant x Emissivity)^(1/4). The function should return the calculated temperature in Kelvin.
"""

import math

def calculate_lava_temperature(heat_flux, stefan_boltzmann_constant, emissivity):
    """
    Calculate the temperature of a lava flow given heat flux, Stefan-Boltzmann Constant, and emissivity.

    Args:
        heat_flux (float): The amount of heat energy transferred per unit area per unit time in W/m^2.
        stefan_boltzmann_constant (float): A physical constant that relates the temperature of an object to the amount of thermal radiation it emits in W/(m^2*K^4).
        emissivity (float): The ability of an object to emit thermal radiation, unitless.

    Returns:
        float: The calculated temperature in Kelvin.
    """
    temperature = heat_flux / (stefan_boltzmann_constant * emissivity)**(1/4)
    return temperature