"""
QUESTION:
Calculate the total number of weights in a neural network given the following conditions: 
- The number of input neurons is a prime number.
- The number of neurons in each hidden layer is a Fibonacci number.
- The number of output neurons is a perfect square.

Create a function `total_weights` that takes four parameters: `input_neurons`, `hidden_layers`, `hidden_neurons`, and `output_neurons`. 

Restrictions: Each weight should be randomly initialized between -1 and 1.
"""

def total_weights(input_neurons, hidden_layers, hidden_neurons, output_neurons):
    """
    Calculate the total number of weights in a neural network given the number of input neurons, 
    hidden layers, neurons in each hidden layer, and output neurons.

    Parameters:
    input_neurons (int): The number of input neurons (a prime number).
    hidden_layers (int): The number of hidden layers.
    hidden_neurons (int): The number of neurons in each hidden layer (a Fibonacci number).
    output_neurons (int): The number of output neurons (a perfect square).

    Returns:
    int: The total number of weights in the neural network.
    """
    # Calculate the number of weights between input layer and first hidden layer
    weights_input_hidden = input_neurons * hidden_neurons
    
    # Calculate the number of weights between each hidden layer
    weights_hidden_hidden = hidden_neurons * hidden_neurons
    
    # Calculate the number of weights between the last hidden layer and output layer
    weights_hidden_output = hidden_neurons * output_neurons
    
    # Calculate the total number of weights
    total_weights = weights_input_hidden + (weights_hidden_hidden * (hidden_layers - 1)) + weights_hidden_output
    
    return total_weights