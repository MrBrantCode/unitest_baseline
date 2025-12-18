"""
QUESTION:
Implement the `dw` function to calculate the change in temperature for a given gas using the isothermal process. The function should take the specific heat ratio (gamma) and a list of initial temperatures as input and return the change in temperature.

The specific heat ratio (gamma) will be a positive non-zero float, and the input list of initial temperatures will have at least one element. The function should calculate the change in temperature using the formula: ΔT = T0 * (1 - 1/γ), where ΔT is the change in temperature, T0 is the initial temperature, and γ is the specific heat ratio.
"""

from typing import List

def dw(gamma: float, initial_temperatures: List[float]) -> float:
    delta_t = initial_temperatures[0] * (1 - 1/gamma)
    return delta_t