"""
QUESTION:
Implement a Naive Bayes classifier that takes into account different types of features and handles zero probabilities. The function should accept a 2D array `data` and a 1D array `classes` as input, where `data` is the training data and `classes` is the target variable. The function should return a function that can be used to make predictions on new data. The function should handle both continuous and categorical features and use Laplace smoothing to prevent issues with features that have not been observed in the training data.
"""

from collections import defaultdict
from math import log
from typing import Callable

def naive_bayes(data: list, classes: list) -> Callable:
    """
    Train a Naive Bayes classifier that handles different types of features and zero probabilities.

    Args:
    data (list): 2D array of training data.
    classes (list): 1D array of target variable.

    Returns:
    Callable: Function to make predictions on new data.
    """

    # Calculate class priors
    class_priors = {}
    for class_label in set(classes):
        class_priors[class_label] = (classes.count(class_label) + 1) / (len(classes) + len(set(classes)))

    # Calculate likelihoods for each feature
    likelihoods = defaultdict(dict)
    for feature_idx, _ in enumerate(data[0]):
        for class_label in set(classes):
            class_data = [row[feature_idx] for row, class_ in zip(data, classes) if class_ == class_label]
            if isinstance(class_data[0], str):  # Categorical feature
                likelihoods[feature_idx][class_label] = {}
                for feature_value in set(class_data):
                    likelihoods[feature_idx][class_label][feature_value] = (class_data.count(feature_value) + 1) / (len(class_data) + len(set(class_data)))
            else:  # Continuous feature
                mean = sum(class_data) / len(class_data)
                variance = sum((x - mean) ** 2 for x in class_data) / len(class_data)
                likelihoods[feature_idx][class_label] = (mean, variance)

    # Define the prediction function
    def predict(new_instance):
        probabilities = {}
        for class_label in class_priors:
            probabilities[class_label] = log(class_priors[class_label])
            for feature_idx, feature_value in enumerate(new_instance):
                if isinstance(feature_value, str):  # Categorical feature
                    probabilities[class_label] += log(likelihoods[feature_idx][class_label].get(feature_value, 1e-9))
                else:  # Continuous feature
                    mean, variance = likelihoods[feature_idx][class_label]
                    probabilities[class_label] += log((1 / (variance ** 0.5)) * (2.71828 ** (-((feature_value - mean) ** 2) / (2 * variance))))
        return max(probabilities, key=probabilities.get)

    return predict