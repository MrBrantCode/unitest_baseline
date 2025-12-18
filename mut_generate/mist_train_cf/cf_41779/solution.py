"""
QUESTION:
Implement a function `calculate_rayleigh_number` that calculates the Rayleigh number for natural convection heat transfer in a vertical channel. The function should take the following parameters: `g` (acceleration due to gravity in m/s^2), `beta` (coefficient of thermal expansion in 1/K), `T_hot` (temperature of the hot surface in K), `T_cold` (temperature of the cold surface in K), `H` (height of the channel in m), `nu` (kinematic viscosity of the fluid in m^2/s), and `alpha` (thermal diffusivity of the fluid in m^2/s). The function should return the calculated Rayleigh number (Ra) using the formula Ra = (g * beta * (T_hot - T_cold) * H**3) / (nu * alpha). Assume all input parameters are positive non-zero real numbers.
"""

import math

def calculate_rayleigh_number(g, beta, T_hot, T_cold, H, nu, alpha):
    Ra = (g * beta * (T_hot - T_cold) * H**3) / (nu * alpha)
    return Ra