"""
QUESTION:
Implement a function `quantum_superposition` that takes a string of bits as input and returns a string representing the superposed state of the input bits.
"""

def quantum_superposition(bits):
    """
    This function takes a string of bits as input and returns a string representing the superposed state of the input bits.
    
    Args:
    bits (str): A string of bits (0s and 1s)
    
    Returns:
    str: A string representing the superposed state of the input bits
    """
    superposed_state = ""
    for bit in bits:
        if bit == '0':
            superposed_state += '0±1'
        elif bit == '1':
            superposed_state += '1±0'
    return superposed_state