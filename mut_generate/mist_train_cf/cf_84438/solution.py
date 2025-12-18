"""
QUESTION:
Determine whether a convolutional neural network $h_3(h_2(h_1(x)))$, where $h_i(x) = V_i x$ and $V_i$ are matrices, can be considered a non-linear network even without activation functions.
"""

def is_non_linear(neural_network_configuration):
    """
    This function determines if a given neural network configuration is non-linear.
    
    Parameters:
    neural_network_configuration (list): A list of dictionaries, each containing 'activation_function' and 'operation' keys.
    
    Returns:
    bool: True if the neural network is non-linear, False otherwise.
    """
    
    for layer in neural_network_configuration:
        if layer['activation_function'] != 'linear':
            return True
    
    return False