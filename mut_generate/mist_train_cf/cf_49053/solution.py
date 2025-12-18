"""
QUESTION:
Create a function `calibrate_imbalanced_dataset` to handle imbalanced datasets when using a calibrator. The function should take into account whether to pass "sample_weights" to the calibrator or not. Note that the base model has already been trained with "sample_weights" to consider the class imbalance. The goal is to determine the correct approach for the calibrator.
"""

def calibrate_imbalanced_dataset(calibrator, X, y, base_model, sample_weights):
    """
    Calibrate a model on an imbalanced dataset.

    Parameters:
    calibrator: The calibrator to be used.
    X (array-like): The input data.
    y (array-like): The target data.
    base_model: The base model that has already been trained with sample_weights.
    sample_weights (array-like, optional): The sample weights for the base model.

    Returns:
    The calibrated model.
    """

    # The base model has already been trained with sample_weights, 
    # so we don't need to pass sample_weights to the calibrator
    # The calibrator's role is to adjust the probabilities predicted by the model
    # rather than learning the weights
    return calibrator.fit(base_model, X, y)