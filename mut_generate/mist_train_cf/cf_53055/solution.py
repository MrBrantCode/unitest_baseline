"""
QUESTION:
Write a function `neural_network_complexity` that calculates the complexity of a neural network, which is represented by the total number of nodes (neurons) in the network. The function should take as input a list of integers, where each integer represents the number of nodes in each layer of the network. The function should return the total number of nodes in the network.
"""

def neural_network_complexity(layer_nodes):
    """
    This function calculates the total number of nodes in a neural network.
    
    Args:
    layer_nodes (list): A list of integers representing the number of nodes in each layer of the network.
    
    Returns:
    int: The total number of nodes in the network.
    """
    return sum(layer_nodes)