"""
QUESTION:
Implement a function named `weighted_binary_cross_entropy_loss` that calculates the weighted binary cross-entropy loss for a given classification problem, where each ground truth label is assigned a different weight and the predicted probabilities are not limited to the range [0, 1]. The function should take three parameters: `labels` (a list or array of ground truth labels), `predictions` (a list or array of predicted probabilities), and `weights` (a list or array of weights assigned to each ground truth label). The function should return the total weighted binary cross-entropy loss.
"""

import numpy as np

def weighted_binary_cross_entropy_loss(labels, predictions, weights):
    loss = 0
    for label, prediction, weight in zip(labels, predictions, weights):
        loss += -(weight * label * np.log(prediction) + (1 - label) * np.log(1 - prediction))
    return loss