"""
QUESTION:
Write a Python function named `quantum_entanglement` that calculates the probability of measuring a qubit in a particular state. The function should take as input the qubit's initial state (represented as a complex number) and the measurement outcome (represented as a binary digit, 0 or 1). The function should return the probability of measuring the qubit in the given state, rounded to 4 decimal places.

Note: The probability of measuring a qubit in a particular state can be calculated using the formula P = |ψ|², where ψ is the qubit's wave function. For simplicity, assume the qubit's wave function is represented by the input complex number.
"""

import cmath

def quantum_entanglement(qubit_state, measurement_outcome):
    """
    Calculate the probability of measuring a qubit in a particular state.

    Args:
    qubit_state (complex): The qubit's initial state, represented as a complex number.
    measurement_outcome (int): The measurement outcome, represented as a binary digit (0 or 1).

    Returns:
    float: The probability of measuring the qubit in the given state, rounded to 4 decimal places.
    """
    # Calculate the probability using the formula P = |ψ|²
    probability = abs(qubit_state)**2
    
    # Since the measurement outcome is either 0 or 1, we can use it to determine the probability
    # If the measurement outcome is 0, the probability is the real part of the qubit state squared
    # If the measurement outcome is 1, the probability is the imaginary part of the qubit state squared
    if measurement_outcome == 0:
        probability = (qubit_state.real**2)
    elif measurement_outcome == 1:
        probability = (qubit_state.imag**2)
    
    # Round the probability to 4 decimal places
    probability = round(probability, 4)
    
    return probability