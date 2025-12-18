"""
QUESTION:
Write a function `is_resilient_to_quantum_attacks` that determines whether a given cryptographic system is resilient to quantum attacks. The function should take as input a cryptographic system (represented as a string) and a list of quantum-resistant algorithms (also represented as strings). The function should return `True` if the cryptographic system is resilient to quantum attacks, and `False` otherwise.
"""

def is_resilient_to_quantum_attacks(cryptographic_system, quantum_resistant_algorithms):
    """
    Determines whether a given cryptographic system is resilient to quantum attacks.

    Args:
        cryptographic_system (str): The cryptographic system to check.
        quantum_resistant_algorithms (list[str]): A list of quantum-resistant algorithms.

    Returns:
        bool: True if the cryptographic system is resilient to quantum attacks, False otherwise.
    """
    return cryptographic_system in quantum_resistant_algorithms