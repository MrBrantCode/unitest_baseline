"""
QUESTION:
Write a Python function named k_fold_cross_validation that performs k-fold cross-validation to assess the performance of a model. The function should take in a model, a dataset X, a target variable y, the number of folds k, and a performance metric as input. It should return the average performance of the model across all folds. Assume that the dataset can be divided exactly into k folds and that the model has a fit method and a predict method. The function should not take any other parameters.
"""

def k_fold_cross_validation(model, X, y, k, performance_metric):
    """
    Performs k-fold cross-validation to assess the performance of a model.

    Args:
    - model: The model to be evaluated.
    - X (list or array): The dataset.
    - y (list or array): The target variable.
    - k (int): The number of folds.
    - performance_metric (function): The performance metric to use.

    Returns:
    - The average performance of the model across all folds.
    """

    # Initialize the list to store the performance of each fold
    performances = []

    # Calculate the size of each fold
    fold_size = len(X) // k

    # Iterate over the k folds
    for i in range(k):
        # Calculate the start and end indices of the current fold
        start = i * fold_size
        end = (i + 1) * fold_size

        # Split the data into the current fold and the rest
        X_current_fold = X[start:end]
        y_current_fold = y[start:end]
        X_train = X[:start] + X[end:]
        y_train = y[:start] + y[end:]

        # Fit the model using the training data
        model.fit(X_train, y_train)

        # Predict the target variable for the current fold
        y_pred = model.predict(X_current_fold)

        # Calculate the performance of the model for the current fold
        performance = performance_metric(y_current_fold, y_pred)

        # Append the performance to the list
        performances.append(performance)

    # Calculate and return the average performance across all folds
    return sum(performances) / k