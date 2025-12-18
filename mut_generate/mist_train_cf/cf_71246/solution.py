"""
QUESTION:
Write a function named `evaluate_model_prediction` that takes a training dataset and a validation dataset as input. The function should calculate the L1 and L2 error metrics on the training dataset and return the results. Also, include a note about the activation function used in the Transformer architecture. The function should not actually train any model or predict on the validation dataset, only calculate error metrics on the training dataset.
"""

def evaluate_model_prediction(training_dataset):
    """
    Calculate the L1 and L2 error metrics on the training dataset.

    Args:
        training_dataset (list of tuples): A list of tuples containing the actual values and predicted values.

    Returns:
        tuple: A tuple containing the L1 error and L2 error.
    """
    # Unpack the actual values and predicted values from the training dataset
    actual_values, predicted_values = zip(*training_dataset)

    # Calculate the L1 error
    l1_error = sum(abs(a - p) for a, p in zip(actual_values, predicted_values)) / len(actual_values)

    # Calculate the L2 error
    l2_error = sum((a - p) ** 2 for a, p in zip(actual_values, predicted_values)) / len(actual_values)

    # Return the L1 and L2 errors
    return l1_error, l2_error