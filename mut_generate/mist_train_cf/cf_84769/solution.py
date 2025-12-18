"""
QUESTION:
Implement a function `create_neural_network` to simulate the basic structure of a neural network. The function should take two parameters: `num_inputs` (the number of neurons in the input layer) and `num_outputs` (the number of neurons in the output layer). The function should create a neural network with one hidden layer containing 2 times the number of neurons in the input layer.
"""

def create_neural_network(num_inputs, num_outputs):
    # Create a neural network with one hidden layer containing 2 times the number of neurons in the input layer
    hidden_layer = 2 * num_inputs
    
    # Define the structure of the neural network
    neural_network = {
        'input_layer': num_inputs,
        'hidden_layer': hidden_layer,
        'output_layer': num_outputs
    }
    
    return neural_network