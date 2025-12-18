"""
QUESTION:
Implement a function called `find_overfitting` that determines whether a given model is overfitting based on its training and test errors. The function should take two parameters: `training_error` and `test_error`, representing the mean squared error of the model on the training and test datasets, respectively. The function should return a boolean value indicating whether the model is overfitting, with `True` indicating overfitting and `False` otherwise. Assume that overfitting occurs when the difference between the test error and training error is greater than 0.1.
"""

def find_overfitting(training_error, test_error):
    """
    Determines whether a given model is overfitting based on its training and test errors.

    Args:
    training_error (float): The mean squared error of the model on the training dataset.
    test_error (float): The mean squared error of the model on the test dataset.

    Returns:
    bool: True if the model is overfitting, False otherwise.
    """
    return test_error - training_error > 0.1