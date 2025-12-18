"""
QUESTION:
Implement the `calculate_sample_weights` function, which takes in the feature matrix `X`, target labels `Y`, dataset split `dataset`, and sample indices `sample_indices`. Calculate the sample weights based on the dataset and the given sample indices, and return the resulting sample weights as a numpy array. The function should only use the provided inputs and should not rely on any external information.
"""

import numpy as np

def calculate_sample_weights(X, Y, dataset, sample_indices):
    """
    Calculate the sample weights based on the dataset and the given sample indices.

    Args:
    X (numpy.ndarray): Feature matrix of the graph nodes
    Y (numpy.ndarray): Target labels for the graph nodes
    dataset (dict): Dictionary containing the dataset split into train, validation, and test sets
    sample_indices (numpy.ndarray): Indices of the samples for which to calculate the weights

    Returns:
    numpy.ndarray: Array of sample weights corresponding to the given sample indices
    """
    class_distribution = np.bincount(Y[dataset['train']['X_idx']])
    class_weights = 1 / class_distribution[Y[dataset['train']['X_idx']]]
    sample_weights = class_weights[sample_indices]
    return sample_weights