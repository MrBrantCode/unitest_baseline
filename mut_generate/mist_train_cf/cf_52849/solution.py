"""
QUESTION:
Implement a function to determine whether TensorFlow can be used for a given machine learning algorithm. The function should take as input the name of the machine learning algorithm and return True if the algorithm can be implemented using TensorFlow, and False otherwise. Restriction: only consider the algorithms decision trees, Random Forests, SVM, Linear/Logistic Regression, K-NN, KMeans, Naive-Bayes.
"""

def can_use_tensorflow(algorithm_name):
    """
    Determine whether TensorFlow can be used for a given machine learning algorithm.

    Args:
    algorithm_name (str): The name of the machine learning algorithm.

    Returns:
    bool: True if the algorithm can be implemented using TensorFlow, False otherwise.
    """
    tensorflow_supported_algorithms = ["Linear Regression", "Logistic Regression", "Naive-Bayes"]
    return algorithm_name in tensorflow_supported_algorithms