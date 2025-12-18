"""
QUESTION:
Write a function `feature_selection_technique` to determine the most suitable feature selection technique for a given dataset, considering the complexities and nuances associated with the process. The function should return the name of the most suitable technique based on the dataset characteristics.
"""

def feature_selection_technique(dataset_characteristics):
    """
    Determine the most suitable feature selection technique for a given dataset.

    Parameters:
    dataset_characteristics (dict): A dictionary containing the characteristics of the dataset.

    Returns:
    str: The name of the most suitable feature selection technique.
    """

    # Replace this with your actual logic to determine the most suitable technique
    # For demonstration purposes, a simple logic is used
    if dataset_characteristics.get('num_features') > 100 and dataset_characteristics.get('num_samples') < 1000:
        return 'Recursive Feature Elimination'
    elif dataset_characteristics.get('num_features') < 100 and dataset_characteristics.get('num_samples') > 1000:
        return 'Lasso Regularization'
    else:
        return 'Forward Selection'