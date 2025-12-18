"""
QUESTION:
Write a function `bayesian_network_params` that calculates the total number of independent parameters in a Bayesian network. The network has 4 nodes (H, U, P, W) with the structure H --> U <-- P <-- W, where each node can take on k distinct values. Assume H and W have no parents, P has 1 parent, and U has 2 parents. The function should take an integer k as input and return the total number of independent parameters.
"""

def bayesian_network_params(k):
    """
    Calculate the total number of independent parameters in a Bayesian network.
    
    The network has 4 nodes (H, U, P, W) with the structure H --> U <-- P <-- W, 
    where each node can take on k distinct values.
    
    Parameters:
    k (int): The number of distinct values each node can take on.
    
    Returns:
    int: The total number of independent parameters in the Bayesian network.
    """
    return 2 * (k - 1) + k * (k - 1) + k * k * (k - 1)