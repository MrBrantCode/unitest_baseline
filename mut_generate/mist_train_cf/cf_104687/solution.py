"""
QUESTION:
Write a function `compute_total_weights` that calculates the total number of weights in a neural network layer given the number of input neurons, the number of hidden layers, the number of neurons in each hidden layer, and the number of output neurons. The function should take four parameters: `input_neurons`, `hidden_layers`, `hidden_neurons`, and `output_neurons`, and return the total number of weights.
"""

def compute_total_weights(input_neurons, hidden_layers, hidden_neurons, output_neurons):
    """
    Calculate the total number of weights in a neural network layer.

    Parameters:
    input_neurons (int): The number of input neurons.
    hidden_layers (int): The number of hidden layers.
    hidden_neurons (int): The number of neurons in each hidden layer.
    output_neurons (int): The number of output neurons.

    Returns:
    int: The total number of weights in the neural network layer.
    """
    # Calculate the number of weights between the input layer and the first hidden layer
    weights_input_hidden = input_neurons * hidden_neurons
    
    # Calculate the number of weights between the hidden layers
    weights_hidden = hidden_neurons * hidden_neurons * (hidden_layers - 1)
    
    # Calculate the number of weights between the last hidden layer and the output layer
    weights_hidden_output = hidden_neurons * output_neurons
    
    # Calculate the total number of weights
    total_weights = weights_input_hidden + weights_hidden + weights_hidden_output
    
    return total_weights