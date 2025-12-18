"""
QUESTION:
Write a function named `lstm_cell` that takes the following inputs: 
- `prev_hidden_state`: the previous hidden state of the LSTM cell
- `prev_cell_state`: the previous cell state of the LSTM cell
- `current_input`: the current input to the LSTM cell
- `weights`: a dictionary containing the weights for the input gate, forget gate, and output gate
- `bias`: a dictionary containing the biases for the input gate, forget gate, and output gate

The function should return the updated hidden state and cell state of the LSTM cell after processing the current input. Assume the sigmoid and tanh activation functions are already implemented.
"""

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return 2 / (1 + np.exp(-2 * x)) - 1

def lstm_cell(prev_hidden_state, prev_cell_state, current_input, weights, bias):
    """
    This function calculates the updated hidden state and cell state of an LSTM cell.

    Parameters:
    prev_hidden_state (numpy array): The previous hidden state of the LSTM cell.
    prev_cell_state (numpy array): The previous cell state of the LSTM cell.
    current_input (numpy array): The current input to the LSTM cell.
    weights (dictionary): A dictionary containing the weights for the input gate, forget gate, and output gate.
    bias (dictionary): A dictionary containing the biases for the input gate, forget gate, and output gate.

    Returns:
    tuple: A tuple containing the updated hidden state and cell state of the LSTM cell.
    """

    # Calculate the forget gate
    forget_gate_input = np.dot(current_input, weights['forget_gate_weights']) + np.dot(prev_hidden_state, weights['forget_gate_weights_hidden']) + bias['forget_gate_bias']
    forget_gate_output = sigmoid(forget_gate_input)

    # Calculate the input gate
    input_gate_input = np.dot(current_input, weights['input_gate_weights']) + np.dot(prev_hidden_state, weights['input_gate_weights_hidden']) + bias['input_gate_bias']
    input_gate_output = sigmoid(input_gate_input)
    input_gate_tanh = tanh(np.dot(current_input, weights['input_gate_weights_tanh']) + np.dot(prev_hidden_state, weights['input_gate_weights_hidden_tanh']) + bias['input_gate_bias_tanh'])

    # Calculate the output gate
    output_gate_input = np.dot(current_input, weights['output_gate_weights']) + np.dot(prev_hidden_state, weights['output_gate_weights_hidden']) + bias['output_gate_bias']
    output_gate_output = sigmoid(output_gate_input)
    output_gate_tanh = tanh(np.dot(current_input, weights['output_gate_weights_tanh']) + np.dot(prev_hidden_state, weights['output_gate_weights_hidden_tanh']) + bias['output_gate_bias_tanh'])

    # Calculate the updated cell state
    cell_state = forget_gate_output * prev_cell_state + input_gate_output * input_gate_tanh

    # Calculate the updated hidden state
    hidden_state = output_gate_output * output_gate_tanh

    return hidden_state, cell_state