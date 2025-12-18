"""
QUESTION:
Write a Python function `compute_metrics` that takes in the following parameters:
- `nmethods` (integer): The number of methods used for predictions.
- `gold_prefs` (list): A list of gold preferences.
- `predictions` (list): A list of predicted rankings.
- `metrics` (dictionary, optional): A dictionary to store the computed metrics. If not provided, it should default to an empty dictionary.
- `nruns` (integer, optional): The number of runs. Defaults to 1.
- `r` (integer, optional): The specific run index. Defaults to 0.

The function should compute accuracy metrics (accuracy and F1 score) for each method and run, using the gold preferences and predicted rankings, and update the `metrics` dictionary with the computed metrics.
"""

import numpy as np

def compute_metrics(nmethods, gold_prefs, predictions, metrics={}, nruns=1, r=0):
    if not metrics:
        metrics['acc'] = np.zeros((nmethods, nruns))
        metrics['f1'] = np.zeros((nmethods, nruns))

    for i in range(nmethods):
        true_positives = sum(1 for j in range(len(gold_prefs)) if gold_prefs[j] == predictions[i][j])
        false_positives = sum(1 for j in range(len(gold_prefs)) if gold_prefs[j] != predictions[i][j])
        false_negatives = sum(1 for j in range(len(gold_prefs)) if gold_prefs[j] != predictions[i][j])

        precision = true_positives / (true_positives + false_positives)
        recall = true_positives / (true_positives + false_negatives)

        accuracy = (true_positives + (len(gold_prefs) - true_positives - false_positives)) / len(gold_prefs)
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        metrics['acc'][i, r] = accuracy
        metrics['f1'][i, r] = f1_score

    return metrics