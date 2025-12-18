"""
QUESTION:
Implement a function named `apply_superposition` that takes two arguments, `state1` and `state2`, representing two states that a particle can be in. The function should return a superposition of the two states, represented as a dictionary where each state is assigned a probability amplitude. The function should ensure that the probabilities of the two states add up to 1.
"""

import math

def apply_superposition(state1, state2):
    """
    This function takes two arguments, state1 and state2, representing two states that a particle can be in.
    It returns a superposition of the two states, represented as a dictionary where each state is assigned a probability amplitude.
    The function ensures that the probabilities of the two states add up to 1.

    Args:
        state1 (str): The first state of the particle.
        state2 (str): The second state of the particle.

    Returns:
        dict: A dictionary representing the superposition of the two states.
    """

    # Calculate the probability amplitude for each state
    amplitude = 1 / math.sqrt(2)

    # Create a dictionary to represent the superposition
    superposition = {
        state1: amplitude,
        state2: amplitude
    }

    return superposition