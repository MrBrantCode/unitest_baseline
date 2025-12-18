"""
QUESTION:
Implement a function `calculate_total_parameters(model)` that calculates the total number of parameters in a given neural network model. The model is expected to have a `parameters()` method that returns an iterator over the model's parameters, and each parameter is expected to have a `numel()` method that returns the number of elements in the parameter tensor. The function should return the total number of parameters as an integer.
"""

def calculate_total_parameters(model):
    """
    Calculate the total number of parameters in the given neural network model.

    Args:
    model: The neural network model for which the parameters need to be calculated.

    Returns:
    int: The total number of parameters in the model.
    """
    total_parameters = sum(p.numel() for p in model.parameters())
    return total_parameters