"""
QUESTION:
Implement a function called `backpropagation_example` that demonstrates the backpropagation algorithm in a simple neural network trained to convert temperatures from Celsius to Fahrenheit, using an initial weight of 0, initial bias of 0, learning rate of 0.01, and a single training set with input 0 and actual output 32. The function should return the updated weight and bias after applying the backpropagation algorithm and gradient descent.
"""

def backpropagation_example(weight, bias, learning_rate, input_data, actual_output):
    output = input_data * weight + bias
    error = (output - actual_output) ** 2
    d_error_d_weight = 2 * (output - actual_output) * input_data
    d_error_d_bias = 2 * (output - actual_output)

    updated_weight = weight - learning_rate * d_error_d_weight
    updated_bias = bias - learning_rate * d_error_d_bias

    return updated_weight, updated_bias