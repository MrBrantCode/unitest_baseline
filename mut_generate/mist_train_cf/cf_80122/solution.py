"""
QUESTION:
Write a Python function `update_weights` that simulates one iteration of the backpropagation algorithm in a neural network to update the weights and minimize the error function. The function should take in the learning rate, weights, and error gradient, and return the updated weights. Assume the error function is differentiable and the weights are updated using gradient descent.
"""

def update_weights(learning_rate, weights, error_gradient):
    """
    Simulates one iteration of the backpropagation algorithm in a neural network 
    to update the weights and minimize the error function.

    Args:
        learning_rate (float): The learning rate for the gradient descent.
        weights (list): The current weights of the neural network.
        error_gradient (list): The gradient of the error function with respect to the weights.

    Returns:
        list: The updated weights.
    """

    # Calculate the weight updates by subtracting the product of the learning rate and the error gradient from the current weights
    weight_updates = [weight - learning_rate * gradient for weight, gradient in zip(weights, error_gradient)]

    return weight_updates