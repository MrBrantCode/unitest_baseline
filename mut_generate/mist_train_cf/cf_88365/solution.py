"""
QUESTION:
Implement a function `weighted_binary_cross_entropy(y_true, y_pred, weights)` that computes the weighted binary cross-entropy loss of a classification problem. The function takes three inputs: `y_true` representing the ground truth labels, `y_pred` representing the predicted probabilities, and `weights` representing non-negative integer weights assigned to each ground truth label. The function should handle cases where the weights are not sorted in ascending order and may contain duplicate values.
"""

import numpy as np

def weighted_binary_cross_entropy(y_true, y_pred, weights):
    # Sort the weights and predicted probabilities
    sorted_indices = np.argsort(weights)
    sorted_weights = np.array(weights)[sorted_indices]
    sorted_y_pred = np.array(y_pred)[sorted_indices]
    
    # Initialize variables
    loss = 0.0
    accumulated_weight = 0
    total_weight = np.sum(weights)
    
    # Iterate through sorted weights and probabilities
    for weight, y in zip(sorted_weights, sorted_y_pred):
        # Compute the weighted binary cross-entropy loss
        loss += weight * (y * np.log(y + 1e-15) + (1 - y) * np.log(1 - y + 1e-15))
        
        # Accumulate weight
        accumulated_weight += weight
        
        # If all weights have been accumulated, break the loop
        if accumulated_weight == total_weight:
            break
    
    # Return the sum of weighted losses
    return -loss / total_weight