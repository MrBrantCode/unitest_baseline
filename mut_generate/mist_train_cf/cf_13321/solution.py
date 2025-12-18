"""
QUESTION:
Implement the k-fold cross-validation algorithm in Python.
"""

def k_fold_cross_validation(dataset, k):
    """
    This function implements the k-fold cross-validation algorithm.

    Args:
        dataset (list): The input dataset.
        k (int): The number of folds.

    Returns:
        list: A list of tuples, where each tuple contains the training set and the test set for each iteration.
    """
    # Calculate the size of each fold
    fold_size = len(dataset) // k
    
    # Initialize an empty list to store the folds
    folds = []
    
    # Iterate k times to create the folds
    for i in range(k):
        # Calculate the start and end indices for the current fold
        start = i * fold_size
        end = (i + 1) * fold_size
        
        # If this is the last fold, include the remaining data points
        if i == k - 1:
            end = len(dataset)
        
        # Create the current fold by taking a slice of the dataset
        fold = dataset[start:end]
        
        # Create the training set by taking all data points not in the current fold
        training_set = dataset[:start] + dataset[end:]
        
        # Append the training set and the current fold as a tuple to the list of folds
        folds.append((training_set, fold))
    
    return folds