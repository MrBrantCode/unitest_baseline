"""
QUESTION:
Define a function `quantum_superposition` that calculates the number of classical bits that can be stored in a quantum computer with a given number of qubits, illustrating the exponential power of quantum superposition. The function should take an integer `n` as input representing the number of qubits and return the number of classical bits that can be stored.

The function should be able to handle a wide range of inputs, but note that extremely large inputs may exceed the limits of computational resources.
"""

def quantum_superposition(n):
    """
    Calculate the number of classical bits that can be stored in a quantum computer with a given number of qubits.

    Parameters:
    n (int): The number of qubits.

    Returns:
    int: The number of classical bits that can be stored.
    """
    return 2 ** n