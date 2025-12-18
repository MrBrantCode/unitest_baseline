"""
QUESTION:
Estimate the total number of parameters in a densely connected neural network with the following architecture: 

- Input layer: 100 dimensions
- Hidden layer 1: 1000 neurons
- Hidden layer 2: 10 neurons
- Output layer: 1 neuron

Each neuron in a layer is connected to every neuron in the previous and next layers. The network does not include batch normalization or learnable parameters within the activation functions.
"""

def calculate_parameters(input_dim, hidden1_dim, hidden2_dim, output_dim):
    """
    Calculate the total number of parameters in a densely connected neural network.

    Args:
    input_dim (int): The number of dimensions in the input layer.
    hidden1_dim (int): The number of neurons in the first hidden layer.
    hidden2_dim (int): The number of neurons in the second hidden layer.
    output_dim (int): The number of neurons in the output layer.

    Returns:
    int: The total number of parameters in the neural network.
    """

    # Calculate the number of parameters from input to hidden layer 1
    params = input_dim * hidden1_dim + hidden1_dim
    
    # Calculate the number of parameters from hidden layer 1 to hidden layer 2
    params += hidden1_dim * hidden2_dim + hidden2_dim
    
    # Calculate the number of parameters from hidden layer 2 to output layer
    params += hidden2_dim * output_dim
    
    return params