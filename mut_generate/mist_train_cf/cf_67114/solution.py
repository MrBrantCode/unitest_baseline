"""
QUESTION:
Create a function called `quantum_superposition` that calculates and returns the number of possible states for a quantum system with a given number of qubits.
"""

def quantum_superposition(qubits):
    """
    This function calculates the number of possible states for a quantum system with a given number of qubits.

    Parameters:
    qubits (int): The number of qubits in the quantum system.

    Returns:
    int: The number of possible states for the quantum system.
    """
    return 2 ** qubits