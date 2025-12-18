"""
QUESTION:
Write a function `calculate_accuracy` that determines whether to use balanced accuracy or common accuracy in a multi-class classification model given the proportion of each class. The function should consider that the model has three classes with significantly different proportions. The function should return the name of the recommended accuracy metric.
"""

def calculate_accuracy(class_proportions):
    """
    Recommends the accuracy metric to use for a multi-class classification model.

    Args:
        class_proportions (list): A list of proportions for each class.

    Returns:
        str: The name of the recommended accuracy metric.
    """
    # Check if the classes are highly imbalanced
    if any(proportion < 0.1 for proportion in class_proportions):
        # If the minor class is significant, recommend balanced accuracy
        return "Balanced Accuracy"
    else:
        # If the classes are relatively balanced, recommend common accuracy
        return "Common Accuracy"