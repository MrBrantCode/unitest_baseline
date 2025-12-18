"""
QUESTION:
Identify the computational procedure that does not belong to the unsupervised learning paradigm within the realm of artificial intelligence. Provide the function name `check_unsupervised` that takes a list of algorithms as input and returns the name of the algorithm that is not an unsupervised learning paradigm.
"""

def check_unsupervised(algorithms):
    """
    Identify the algorithm that does not belong to the unsupervised learning paradigm.

    Args:
    algorithms (list): A list of algorithm names.

    Returns:
    str: The name of the algorithm that is not an unsupervised learning paradigm.
    """
    # List of supervised learning algorithms
    supervised_algorithms = ["retraining a neural network", "linear regression", "decision trees", "support vector machines", "logistic regression"]
    
    # Iterate over the input algorithms
    for algorithm in algorithms:
        # Check if the algorithm is a supervised learning algorithm
        if algorithm.lower() in supervised_algorithms:
            return algorithm

    # If no supervised learning algorithm is found, return None
    return None