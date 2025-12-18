"""
QUESTION:
Write a function called `is_entangled` that takes two arguments, `qubit1` and `qubit2`, representing the states of two qubits. The function should return `True` if the qubits are entangled and `False` otherwise. The function should assume that the qubits are represented as lists of two elements, where the first element is the coefficient of the 0 state and the second element is the coefficient of the 1 state. The function should also assume that the coefficients are complex numbers.
"""

def is_entangled(qubit1, qubit2):
    """
    This function checks if two qubits are entangled.

    Args:
    qubit1 (list): A list of two complex numbers representing the state of the first qubit.
    qubit2 (list): A list of two complex numbers representing the state of the second qubit.

    Returns:
    bool: True if the qubits are entangled, False otherwise.
    """
    # Compute the coefficients of the four basis states
    a, b = qubit1
    c, d = qubit2
    
    # Check if the qubits are separable
    if a * d == b * c:
        return False
    else:
        return True