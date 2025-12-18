"""
QUESTION:
Write a function `calculate_total_parameters` that calculates the total number of parameters in a recurrent neural network. The network consists of two LSTM layers with units `lstm_units_1` and `lstm_units_2`, a fully connected layer with `fc_neurons` neurons, and a softmax layer with `num_categories` response categories. The input sequence consists of 100 words, each represented by a `word_vector_dim`-dimensional word vector.
"""

def calculate_total_parameters(word_vector_dim, lstm_units_1, lstm_units_2, fc_neurons, num_categories):
    """
    Calculate the total number of parameters in a recurrent neural network.

    Parameters:
    word_vector_dim (int): The dimensions of the word vectors.
    lstm_units_1 (int): The number of LSTM units in the first layer.
    lstm_units_2 (int): The number of LSTM units in the second layer.
    fc_neurons (int): The number of neurons in the fully connected layer.
    num_categories (int): The number of response categories in the softmax layer.

    Returns:
    int: The total number of parameters in the network.
    """
    # Calculate the parameters for the first LSTM layer
    lstm_1_params = 4 * ((word_vector_dim + 1) * lstm_units_1 + lstm_units_1**2)
    
    # Calculate the parameters for the second LSTM layer
    lstm_2_params = 4 * ((lstm_units_1 + 1) * lstm_units_2 + lstm_units_2**2)
    
    # Calculate the parameters for the fully connected layer
    fc_params = (lstm_units_2 + 1) * fc_neurons
    
    # Calculate the parameters for the softmax layer
    softmax_params = (fc_neurons + 1) * num_categories
    
    # Return the total number of parameters
    return lstm_1_params + lstm_2_params + fc_params + softmax_params