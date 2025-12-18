"""
QUESTION:
Implement the `grover_search` function to simulate Grover's algorithm for searching an element in a database of size N and compare its performance with classical search algorithms. The function should take an integer `N` as input and return the time complexity of Grover's algorithm and the best classical search algorithm. Assume that the classical search algorithm has a time complexity of O(log N) and Grover's algorithm has a time complexity of O(sqrt(N)). The function should not simulate the actual search process, but rather calculate and return the time complexities.
"""

import math

def grover_search(N):
    """
    Calculate the time complexity of Grover's algorithm and the best classical search algorithm.

    Args:
    N (int): The size of the database.

    Returns:
    tuple: A tuple containing the time complexity of Grover's algorithm and the best classical search algorithm.
    """
    grover_complexity = f"O(sqrt({N}))"
    classical_complexity = f"O(log {N})"
    
    return grover_complexity, classical_complexity