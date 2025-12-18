"""
QUESTION:
Write a function named `quantum_superposition` that takes in a string of binary digits (0s and 1s) and returns all possible combinations of superpositions represented as a list of strings. The function should not take any other parameters and must return the superpositions as a list of strings, where each string represents a possible state of the qubits.
"""

def quantum_superposition(s):
    """
    This function generates all possible combinations of superpositions 
    represented as a list of strings from a given string of binary digits.
    
    Parameters:
    s (str): A string of binary digits (0s and 1s).
    
    Returns:
    list: A list of strings, where each string represents a possible state of the qubits.
    """
    
    # Base case: If the string is empty, return a list containing an empty string
    if len(s) == 0:
        return ['']
    
    # Recursive case: If the string is not empty, consider two possibilities for the first bit
    else:
        # Initialize an empty list to store the result
        result = []
        
        # Consider the case where the first bit is 0
        for sub in quantum_superposition(s[1:]):
            result.append('0' + sub)
        
        # Consider the case where the first bit is 1
        for sub in quantum_superposition(s[1:]):
            result.append('1' + sub)
        
        # Consider the case where the first bit is in a superposition (both 0 and 1)
        for sub in quantum_superposition(s[1:]):
            result.append('-' + sub)  # '-' denotes a superposition of 0 and 1
        
        # Return the result
        return result