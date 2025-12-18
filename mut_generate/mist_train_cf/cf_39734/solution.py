"""
QUESTION:
Write a function `calculate_f1_score(dataset)` that takes in a 2D list `dataset` where each row represents a class and contains four values in the order of true positive (TP), false positive (FP), true negative (TN), and false negative (FN). The function should return a list of F1 scores for each class and the macro F1 score. The F1 score is calculated as 2 * (precision * recall) / (precision + recall), where precision is TP / (TP + FP) and recall is TP / (TP + FN). If a denominator is zero, the corresponding precision, recall, or F1 score is zero.
"""

def calculate_f1_score(dataset):
    f1_scores = []
    precision = []
    recall = []
    
    for values in dataset:
        tp, fp, tn, fn = values
        precision.append(0 if (tp + fp) == 0 else tp / (tp + fp))
        recall.append(0 if (tp + fn) == 0 else tp / (tp + fn))
    
    for p, r in zip(precision, recall):
        f1_scores.append(0 if (p + r) == 0 else 2 * (p * r) / (p + r))
    
    macro_f1 = sum(f1_scores) / len(f1_scores)
    
    return f1_scores, macro_f1