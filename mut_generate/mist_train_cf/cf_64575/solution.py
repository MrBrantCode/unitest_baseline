"""
QUESTION:
Implement a function called `quantum_superposition` that calculates the probability of a quantum particle being in a superposition state.
"""

import math

def quantum_superposition(probability_array):
    """
    This function calculates the probability of a quantum particle being in a superposition state.

    Args:
    probability_array (list): A list of probabilities of a quantum particle being in different states.

    Returns:
    float: The probability of the quantum particle being in a superposition state.
    """
    # Calculate the square of the absolute value of each probability
    squared_probabilities = [abs(p)**2 for p in probability_array]
    
    # Calculate the sum of the squared probabilities
    sum_squared_probabilities = sum(squared_probabilities)
    
    # Calculate the probability of the quantum particle being in a superposition state
    superposition_probability = 1 - sum_squared_probabilities
    
    return superposition_probability