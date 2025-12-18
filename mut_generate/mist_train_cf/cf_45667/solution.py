"""
QUESTION:
You are given a string of 1s and 0s and an integer n. Write a function named `qubit_superposition` that takes this string and the integer as input and returns the total number of possible states for n qubits, given that each qubit can be in a superposition of 0 and 1.
"""

def qubit_superposition(string, n):
    """
    This function calculates the total number of possible states for n qubits.
    
    Parameters:
    string (str): A string of 1s and 0s.
    n (int): The number of qubits.
    
    Returns:
    int: The total number of possible states for n qubits.
    """
    return 2 ** n