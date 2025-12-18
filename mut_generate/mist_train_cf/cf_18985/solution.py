"""
QUESTION:
Write a function `weighted_binary_cross_entropy_loss` that calculates the weighted binary cross-entropy loss for a given classification problem. The function takes in three parameters: `labels`, `predictions`, and `weights`, where `labels` is an array of binary ground truth labels (0 or 1), `predictions` is an array of predicted probabilities, and `weights` is an array of weights assigned to each ground truth label. The function should return the total weighted binary cross-entropy loss.
"""

import numpy as np

def weighted_binary_cross_entropy_loss(labels, predictions, weights):
    loss = 0
    for label, prediction, weight in zip(labels, predictions, weights):
        loss += -(weight * label * np.log(prediction) + (1 - label) * np.log(1 - prediction))
    return loss