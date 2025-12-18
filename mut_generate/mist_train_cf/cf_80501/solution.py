"""
QUESTION:
Write a Python function `calculate_auc` to demonstrate how the Area Under the Curve (AUC) changes with an increase in True Positive Rate (TPR) while keeping False Positive Rate (FPR) constant. Assume the AUC is calculated using the trapezoidal rule. 

Restrictions: Use a list of TPR values and a constant FPR value as input, and return the calculated AUC value.
"""

def calculate_auc(tpr_values, fpr):
    """
    Calculate the Area Under the Curve (AUC) using the trapezoidal rule.

    Args:
    tpr_values (list): A list of True Positive Rate (TPR) values.
    fpr (float): A constant False Positive Rate (FPR) value.

    Returns:
    float: The calculated AUC value.
    """
    auc = 0
    for i in range(1, len(tpr_values)):
        base = fpr / (len(tpr_values) - 1)
        height = (tpr_values[i] + tpr_values[i - 1]) / 2
        auc += base * height
    return auc