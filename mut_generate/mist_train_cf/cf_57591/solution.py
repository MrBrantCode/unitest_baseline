"""
QUESTION:
Create a function named `analyze_confusion_matrix` that takes a 2x2 confusion matrix as input, and returns the true positive, false positive, true negative, and false negative values.
"""

def analyze_confusion_matrix(confusion_matrix):
    """
    Analyzes a 2x2 confusion matrix and returns the true positive, false positive, true negative, and false negative values.

    Args:
        confusion_matrix (list): A 2x2 list of lists representing the confusion matrix.

    Returns:
        tuple: A tuple containing the true positive, false positive, true negative, and false negative values.
    """
    TP = confusion_matrix[1][1]
    FP = confusion_matrix[0][1]
    TN = confusion_matrix[0][0]
    FN = confusion_matrix[1][0]

    return TP, FP, TN, FN