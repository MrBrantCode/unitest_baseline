"""
QUESTION:
Write a function `naive_bayes_multiclass` that implements a Naive Bayes classifier for multiclass classification, utilizing Laplace smoothing to handle zero frequency cases. The function should take as input the training data and their corresponding class labels, and return the predicted class label for a given test instance. Assume the features are independent and contribute equally to the output.
"""

import numpy as np

def naive_bayes_multiclass(train_data, train_labels, test_instance, k=1):
    """
    Naive Bayes classifier for multiclass classification with Laplace smoothing.

    Args:
    - train_data (list of lists): Training data.
    - train_labels (list): Corresponding class labels for the training data.
    - test_instance (list): Test instance to predict the class label for.
    - k (int, optional): Smoothing constant. Defaults to 1.

    Returns:
    - int: Predicted class label for the test instance.
    """

    # Get the unique classes and their counts
    unique_classes, class_counts = np.unique(train_labels, return_counts=True)

    # Calculate the prior probabilities for each class
    prior_probabilities = class_counts / len(train_labels)

    # Initialize a dictionary to store the feature probabilities for each class
    feature_probabilities = {}

    # Calculate the feature probabilities for each class
    for i, unique_class in enumerate(unique_classes):
        class_data = [data for data, label in zip(train_data, train_labels) if label == unique_class]

        # Calculate the feature probabilities using Laplace smoothing
        feature_probabilities[unique_class] = [(np.sum(feature) + k) / (class_counts[i] + k * len(test_instance)) for feature in zip(*class_data)]

    # Calculate the posterior probabilities for each class
    posterior_probabilities = []
    for i, unique_class in enumerate(unique_classes):
        posterior_probability = prior_probabilities[i]
        for j, feature in enumerate(test_instance):
            posterior_probability *= feature_probabilities[unique_class][j] if feature else (1 - feature_probabilities[unique_class][j])
        posterior_probabilities.append(posterior_probability)

    # Return the class with the highest posterior probability
    return unique_classes[np.argmax(posterior_probabilities)]