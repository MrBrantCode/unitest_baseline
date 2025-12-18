"""
QUESTION:
Implement a function called 'is_superposition' to determine whether a given quantum state is in a superposition. The function should take a list of complex numbers representing the amplitudes of the quantum state as input. The function should return True if the state is in a superposition, False otherwise. Assume the input list is a valid quantum state, i.e., the sum of the squared absolute values of the amplitudes equals 1. The function should be efficient and well-documented.
"""

def is_superposition(state):
    """
    Determines whether a given quantum state is in a superposition.

    Args:
    state (list): A list of complex numbers representing the amplitudes of the quantum state.

    Returns:
    bool: True if the state is in a superposition, False otherwise.
    """
    # Check if all amplitudes are zero except one
    return len([abs(a) for a in state if abs(a) > 0]) > 1