"""
QUESTION:
Write a function called `quantum_superposition` that calculates the number of possible outcomes for a given number of qubits. A qubit can exist in multiple states (0 and 1) at the same time, thanks to quantum superposition. The function should take an integer `n` as input, representing the number of qubits, and return the total number of possible outcomes, which is 2^n.
"""

def quantum_superposition(n):
    """
    This function calculates the number of possible outcomes for a given number of qubits.

    Args:
        n (int): The number of qubits.

    Returns:
        int: The total number of possible outcomes.
    """
    return 2 ** n