"""
QUESTION:
Implement the `cross_entropy` and `cross_entropy_gradient` functions in Python using NumPy. 

The `cross_entropy(y, y_)` function should take two NumPy arrays `y` and `y_` as input, representing the predicted and true probability distributions, respectively, and return the cross-entropy loss as a scalar value using the formula \( H(y, y') = -\sum_{i} y_i' \log(y_i) \).

The `cross_entropy_gradient(grad_arr, y_arr, label)` function should take three NumPy arrays `grad_arr`, `y_arr`, and `label` as input, representing the gradient array, predicted probability distribution, and true labels, respectively, and store the gradient of the cross-entropy loss with respect to the predicted probability distribution in `grad_arr` using the formula \( \frac{\partial H(y, y')}{\partial y} = -\frac{y'}{y} \). 

Ensure both functions handle input validation and type checking for the input arrays.
"""

import numpy as np

def cross_entropy(y, y_):
    """
    Calculate the cross-entropy loss between predicted and true probability distributions.

    Args:
    y (np.ndarray): Predicted probability distribution.
    y_ (np.ndarray): True probability distribution.

    Returns:
    float: Cross-entropy loss.
    """
    assert isinstance(y, np.ndarray) and isinstance(y_, np.ndarray), "Input should be NumPy arrays"
    assert y.shape == y_.shape, "Input arrays should have the same shape"
    
    # Calculate cross-entropy loss
    loss = -np.sum(y_ * np.log(y))
    return loss


def cross_entropy_gradient(grad_arr, y_arr, label):
    """
    Calculate the gradient of the cross-entropy loss with respect to the predicted probability distribution.

    Args:
    grad_arr (np.ndarray): Gradient array to store the result.
    y_arr (np.ndarray): Predicted probability distribution.
    label (np.ndarray): True labels.

    Returns:
    None
    """
    assert isinstance(grad_arr, np.ndarray) and isinstance(y_arr, np.ndarray) and isinstance(label, np.ndarray), "Inputs should be NumPy arrays"
    assert grad_arr.shape == y_arr.shape == label.shape, "Input arrays should have the same shape"
    
    # Calculate cross-entropy gradient
    gradient = -label / y_arr
    np.copyto(grad_arr, gradient)  # Store the result in grad_arr