"""
QUESTION:
Implement a function named `calculate_auc` that takes two array-like inputs `fpr` (false positive rate data) and `tpr` (true positive rate data) and returns the area under the ROC curve (AUC) using the trapezoidal rule. The function should sort the data points by increasing `fpr` and calculate the AUC by approximating the curve as a series of trapezoids.
"""

import pandas as pd

def calculate_auc(fpr, tpr):
    """
    Calculate the area under the ROC curve using the trapezoidal rule.

    Args:
    fpr (array-like): False positive rate data.
    tpr (array-like): True positive rate data.

    Returns:
    float: Area under the ROC curve (AUC).
    """
    # Sort the data points by increasing FPR
    order = fpr.argsort()
    fpr = fpr[order]
    tpr = tpr[order]

    # Calculate the AUC using the trapezoidal rule
    auc = 0
    for i in range(1, len(fpr)):
        auc += (fpr[i] - fpr[i-1]) * (tpr[i] + tpr[i-1]) / 2

    return auc