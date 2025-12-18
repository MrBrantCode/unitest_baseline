"""
QUESTION:
Implement a function named `calculate_precision_recall` that takes two lists (`predictions` and `labels`) of equal length as input, where each element in the lists represents the predicted and actual label for an instance. The function should calculate the precision and recall metrics on the entity level, as well as the 'macro' average on well-defined classes.

The precision and recall should be calculated using the formulas: Precision = TP / (TP + FP) and Recall = TP / (TP + FN), where TP, FP, and FN represent true positives, false positives, and false negatives, respectively. The 'macro' average should be calculated as the average of precision and recall for each class. The function should return three values: precision, recall, and macro average. Assume that the input lists contain binary labels (0 and 1).
"""

def calculate_precision_recall(predictions, labels):
    """
    Calculate precision and recall metrics on the entity level, as well as the 'macro' average on well-defined classes.

    Args:
    predictions (list): List of predicted labels for each instance.
    labels (list): List of true labels for each instance.

    Returns:
    precision (float): Precision metric.
    recall (float): Recall metric.
    macro_avg (tuple): 'Macro' average on well-defined classes as a tuple of macro precision and macro recall.
    """
    true_positives = sum(1 for p, l in zip(predictions, labels) if p == 1 and l == 1)
    false_positives = sum(1 for p, l in zip(predictions, labels) if p == 1 and l == 0)
    false_negatives = sum(1 for p, l in zip(predictions, labels) if p == 0 and l == 1)

    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0

    true_positives_per_class = [sum(1 for p, l in zip(predictions, labels) if p == c and l == c) for c in set(labels)]
    false_positives_per_class = [sum(1 for p, l in zip(predictions, labels) if p == c and l != c) for c in set(labels)]
    false_negatives_per_class = [sum(1 for p, l in zip(predictions, labels) if p != c and l == c) for c in set(labels)]

    precision_per_class = [tp / (tp + fp) if (tp + fp) > 0 else 0 for tp, fp in zip(true_positives_per_class, false_positives_per_class)]
    recall_per_class = [tp / (tp + fn) if (tp + fn) > 0 else 0 for tp, fn in zip(true_positives_per_class, false_negatives_per_class)]

    macro_precision = sum(precision_per_class) / len(precision_per_class)
    macro_recall = sum(recall_per_class) / len(recall_per_class)

    return precision, recall, (macro_precision, macro_recall)