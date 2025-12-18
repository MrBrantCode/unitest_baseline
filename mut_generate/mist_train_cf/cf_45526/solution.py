"""
QUESTION:
Design a function called `evaluate_network_complexity` that determines the impact of a neural network's architecture on the balance between underfitting and overfitting. The function should take in the number of layers and the number of nodes in each layer as inputs, and return a value that represents the network's complexity. The function should also consider the choice of activation function as a factor in the network's complexity. The function should not consider other factors such as dropout rate, weight initialization, and learning rate.
"""

def evaluate_network_complexity(num_layers, num_nodes_per_layer, activation_function):
    """
    Evaluate the complexity of a neural network based on its architecture.

    Args:
    num_layers (int): The number of layers in the network.
    num_nodes_per_layer (list): A list of the number of nodes in each layer.
    activation_function (str): The activation function used in the network.

    Returns:
    float: A value representing the network's complexity.
    """
    
    # Assign complexity scores to different activation functions
    activation_complexity = {'relu': 1, 'sigmoid': 2, 'tanh': 3}
    
    # Calculate the total number of nodes in the network
    total_nodes = sum(num_nodes_per_layer)
    
    # Calculate the network complexity based on the number of layers, nodes, and activation function
    complexity = num_layers * total_nodes * activation_complexity.get(activation_function, 1)
    
    return complexity