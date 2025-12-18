"""
QUESTION:
Write a function called `detect_overfitting` that takes two accuracy values as input: `training_accuracy` and `validation_accuracy`. The function should return `True` if the model is overfitting (i.e., the difference between `training_accuracy` and `validation_accuracy` is greater than 10%) and `False` otherwise.
"""

def detect_overfitting(training_accuracy, validation_accuracy):
    """
    This function determines if a model is overfitting based on the difference between 
    its training accuracy and validation accuracy.

    Args:
        training_accuracy (float): The accuracy of the model on the training data.
        validation_accuracy (float): The accuracy of the model on the validation data.

    Returns:
        bool: True if the model is overfitting, False otherwise.
    """

    # Calculate the difference between the training accuracy and validation accuracy
    accuracy_difference = abs(training_accuracy - validation_accuracy)

    # If the difference is greater than 10%, return True (model is overfitting)
    # Otherwise, return False
    return accuracy_difference > 0.10