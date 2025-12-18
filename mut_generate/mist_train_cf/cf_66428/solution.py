"""
QUESTION:
Implement the KFold function that takes in a dataset and the number of folds (k) as inputs, and returns the training and test sets for each fold. The function should divide the dataset into 'k' subsets, use one subset as the test set and the rest as the training set, and repeat this process k times.
"""

import numpy as np

def kfold(dataset, k):
    """
    K-fold Cross Validation function.

    Args:
        dataset (list): The input dataset.
        k (int): The number of folds.

    Returns:
        list: A list of tuples containing the training and test sets for each fold.
    """
    # Calculate the size of each fold
    fold_size = len(dataset) // k

    # Initialize an empty list to store the folds
    folds = []

    # Loop through the dataset to create the folds
    for i in range(k):
        # Calculate the start and end indices for the current fold
        start = i * fold_size
        end = (i + 1) * fold_size

        # If this is the last fold, include the remaining data
        if i == k - 1:
            end = len(dataset)

        # Create the test set for the current fold
        test_set = dataset[start:end]

        # Create the training set for the current fold
        train_set = dataset[:start] + dataset[end:]

        # Add the training and test sets to the list of folds
        folds.append((train_set, test_set))

    return folds