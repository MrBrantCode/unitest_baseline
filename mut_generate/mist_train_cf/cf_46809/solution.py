"""
QUESTION:
Implement the function `quantum_entanglement` to calculate the number of entangled particles in a quantum system. The function takes an integer `n` as input, representing the total number of particles in the system, and returns the number of entangled particles. Assume that the number of entangled particles is half the total number of particles if the total number of particles is even, and one more than half the total number of particles if the total number of particles is odd.
"""

def quantum_entanglement(n):
    """
    Calculate the number of entangled particles in a quantum system.
    
    Args:
    n (int): The total number of particles in the system.
    
    Returns:
    int: The number of entangled particles.
    """
    if n % 2 == 0:
        return n // 2
    else:
        return n // 2 + 1