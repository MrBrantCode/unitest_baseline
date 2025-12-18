"""
QUESTION:
Create a Python function `calculate_total_impedance(components)` that takes a list of electrical components and their values, and returns the total impedance of the circuit. The input `components` is a list of tuples, where each tuple contains the component type (R, L, or C) and its value. The total impedance should be calculated based on the combination of the provided components using the formulas for series and parallel circuits: Zs = R + jωL + 1/(jωC) and 1/Zp = 1/R + 1/(jωL) + jωC. Assume ω is a given angular frequency and j is the imaginary unit.
"""

import cmath

def calculate_total_impedance(components, omega):
    """
    Calculate the total impedance of a circuit given a list of electrical components and their values.

    Parameters:
    components (list): A list of tuples, where each tuple contains the component type (R, L, or C) and its value.
    omega (float): The angular frequency.

    Returns:
    complex: The total impedance of the circuit.
    """
    total_impedance = complex(0, 0)
    for component, value in components:
        if component == 'R':
            total_impedance += value
        elif component == 'L':
            total_impedance += 1j * omega * value
        elif component == 'C':
            total_impedance += 1 / (1j * omega * value)

    return total_impedance