"""
QUESTION:
Implement the function `calculate_true_negatives(y_true, y_pred)` that calculates the true negative values for a multilabel classification problem. The function takes two parameters: 
- `y_true`: A 2D array representing the true labels for each instance, where 1 represents the presence of a label and 0 represents its absence.
- `y_pred`: A 2D array representing the predicted labels for each instance, following the same format as `y_true`.

The function should return a 1D array containing the true negative values for each label, which represent the number of instances where the predicted label is not present in the true labels for each label.
"""

def calculate_true_negatives(y_true, y_pred):
    true_negatives = []
    for label in range(len(y_true[0])):
        tn_count = sum(1 for i in range(len(y_true)) if y_true[i][label] == 0 and y_pred[i][label] == 0)
        true_negatives.append(tn_count)
    return true_negatives