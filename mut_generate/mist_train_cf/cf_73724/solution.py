"""
QUESTION:
Implement a function `train_gaussian_classifier` that trains a Gaussian-based Bayes optimal classifier on a dataset with a fixed number of attributes. The function should be able to handle a large number of records in the dataset and should ideally have a time complexity linear to the number of records. Assume that the true distributions of the data are available or can be estimated accurately.
"""

import numpy as np

def train_gaussian_classifier(X, y):
    """
    Trains a Gaussian-based Bayes optimal classifier on a dataset.

    Parameters:
    X (numpy array): The feature dataset.
    y (numpy array): The target variable.

    Returns:
    A dictionary containing the means and covariance matrices for each class.
    """

    # Get unique classes and number of classes
    classes = np.unique(y)
    num_classes = len(classes)

    # Initialize dictionary to store parameters for each class
    params = {}

    # Iterate over each class
    for c in classes:
        # Get the indices of the current class
        indices = np.where(y == c)[0]

        # Get the data for the current class
        X_c = X[indices, :]

        # Calculate the mean of the current class
        mean_c = np.mean(X_c, axis=0)

        # Calculate the covariance matrix of the current class
        cov_c = np.cov(X_c, rowvar=False)

        # Store the mean and covariance matrix in the dictionary
        params[c] = {'mean': mean_c, 'cov': cov_c}

    return params