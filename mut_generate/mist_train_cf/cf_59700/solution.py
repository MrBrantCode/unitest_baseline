"""
QUESTION:
Create a function called "quantum_superposition" that calculates the number of possible states a qubit can exist in. Assume the qubit can be in one of two states (0 or 1) and can exist in multiple states simultaneously until it is measured. The function should take an integer "n" as input, representing the number of qubits, and return the total number of possible states.
"""

def quantum_superposition(n):
    """
    Calculate the number of possible states a qubit can exist in.

    Args:
    n (int): The number of qubits.

    Returns:
    int: The total number of possible states.
    """
    return 2 ** n