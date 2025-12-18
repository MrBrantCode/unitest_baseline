"""
QUESTION:
Write a function `quantum_superposition` that takes an integer `n` as input and returns the number of possible superposition states for a quantum system with `n` entities. The function should use the formula 2^n to calculate the number of possible states.
"""

def quantum_superposition(n):
    """
    Calculate the number of possible superposition states for a quantum system with n entities.

    Args:
    n (int): The number of entities in the quantum system.

    Returns:
    int: The number of possible superposition states.
    """
    return 2 ** n