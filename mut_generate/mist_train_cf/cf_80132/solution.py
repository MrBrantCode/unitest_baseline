"""
QUESTION:
Implement a function `evaluate_classification_metrics` that takes `true_positives`, `false_positives`, and `false_negatives` as inputs and returns the F1 score. Additionally, the function should be able to calculate the Area Under the Receiver Operating Characteristic curve (AUC-ROC) given `true_positive_rates` and `false_positive_rates` for different thresholds.
"""

def evaluate_classification_metrics(true_positives, false_positives, false_negatives, true_positive_rates=None, false_positive_rates=None):
    """
    Calculate F1 score and Area Under the Receiver Operating Characteristic curve (AUC-ROC) if thresholds are provided.

    Args:
    - true_positives (int): Number of true positives.
    - false_positives (int): Number of false positives.
    - false_negatives (int): Number of false negatives.
    - true_positive_rates (list, optional): List of true positive rates for different thresholds. Defaults to None.
    - false_positive_rates (list, optional): List of false positive rates for different thresholds. Defaults to None.

    Returns:
    - dict: Dictionary containing F1 score and AUC-ROC (if thresholds are provided).
    """
    
    # Calculate precision
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) != 0 else 0
    
    # Calculate recall
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) != 0 else 0
    
    # Calculate F1 score
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
    
    # Initialize AUC-ROC to None
    auc_roc = None
    
    # Calculate AUC-ROC if thresholds are provided
    if true_positive_rates is not None and false_positive_rates is not None:
        # Use trapezoidal rule to approximate the area under the ROC curve
        auc_roc = 0
        for i in range(1, len(true_positive_rates)):
            auc_roc += (false_positive_rates[i] - false_positive_rates[i-1]) * (true_positive_rates[i-1] + true_positive_rates[i]) / 2
    
    # Return F1 score and AUC-ROC
    return {"F1 score": f1_score, "AUC-ROC": auc_roc}