"""
QUESTION:
Create a function called `weighted_cross_entropy_loss` that calculates the weighted cross-entropy loss for a given classification problem. The function should take three parameters: `ground_truth`, a list of ground truth labels; `predicted`, a list of predicted probabilities; and `weights`, a list of weights assigned to each label. The function should return the overall weighted cross-entropy loss. The formula for the cross-entropy loss is L = - (y * log(p) + (1 - y) * log(1 - p)), where y is the ground truth label and p is the predicted probability. The weighted loss for each sample is calculated by multiplying the cross-entropy loss by the corresponding weight. The overall weighted cross-entropy loss is the sum of all weighted losses.
"""

import numpy as np

def weighted_cross_entropy_loss(ground_truth, predicted, weights):
    """
    This function calculates the weighted cross-entropy loss for a given classification problem.

    Parameters:
    ground_truth (list): A list of ground truth labels.
    predicted (list): A list of predicted probabilities.
    weights (list): A list of weights assigned to each label.

    Returns:
    float: The overall weighted cross-entropy loss.
    """
    
    # Calculate the cross-entropy loss for each sample
    # We use np.log to compute the natural logarithm
    # We use np.clip to avoid dividing by zero or taking the log of zero
    losses = - (np.multiply(ground_truth, np.log(np.clip(predicted, 1e-7, 1))) + 
                np.multiply(1 - ground_truth, np.log(np.clip(1 - predicted, 1e-7, 1))))
    
    # Calculate the weighted loss for each sample
    weighted_losses = np.multiply(losses, weights)
    
    # Calculate the overall weighted cross-entropy loss
    overall_loss = np.sum(weighted_losses)
    
    return overall_loss