"""
QUESTION:
Write a function `check_qml_principle` that determines whether a given principle corresponds with the basic doctrines of quantum machine learning. The function should take a string representing the principle and return `True` if it corresponds with quantum machine learning principles and `False` otherwise.
"""

def check_qml_principle(principle):
    """
    This function determines whether a given principle corresponds with the basic doctrines of quantum machine learning.

    Parameters:
    principle (str): A string representing the principle to be checked.

    Returns:
    bool: True if the principle corresponds with quantum machine learning principles, False otherwise.
    """
    qml_principles = [
        "Quantum Superposition", 
        "Quantum Entanglement", 
        "Quantum Tunneling", 
        "Scaling Advantage", 
        "No Cloning Theorem", 
        "Uncertainty Principle"
    ]
    return principle in qml_principles