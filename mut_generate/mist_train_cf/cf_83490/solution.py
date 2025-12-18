"""
QUESTION:
Write a function `avoid_overfitting` that takes in a dataset size and a model complexity as input. The function should return a string indicating whether the model is at risk of overfitting or underfitting based on the given dataset size and model complexity.

Assume that a dataset size of less than 1000 and a model complexity of more than 10 is a recipe for overfitting, while a model complexity of less than 5 is prone to underfitting.
"""

def avoid_overfitting(dataset_size, model_complexity):
    """
    Determine whether a model is at risk of overfitting or underfitting.

    Args:
        dataset_size (int): The size of the dataset.
        model_complexity (int): The complexity of the model.

    Returns:
        str: A string indicating whether the model is at risk of overfitting or underfitting.
    """

    # Check for overfitting
    if dataset_size < 1000 and model_complexity > 10:
        return "overfitting"
    
    # Check for underfitting
    elif model_complexity < 5:
        return "underfitting"
    
    # If neither condition is met, the model is likely to be a good fit
    else:
        return "good fit"