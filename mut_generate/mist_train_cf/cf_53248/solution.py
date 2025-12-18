"""
QUESTION:
Define a function `is_overfitted` that takes in two parameters: `train_error` and `test_error`, which represent the error rates of a model on the training data and testing data respectively. The function should return `True` if the model is overfitted and `False` otherwise. Assume that overfitting occurs when the difference between the test error and the train error is greater than 10 percentage points.
"""

def is_overfitted(train_error, test_error):
    """
    Checks if a model is overfitted based on the difference between its train and test errors.

    Args:
    train_error (float): The error rate of the model on the training data.
    test_error (float): The error rate of the model on the testing data.

    Returns:
    bool: True if the model is overfitted, False otherwise.
    """
    return test_error - train_error > 0.1