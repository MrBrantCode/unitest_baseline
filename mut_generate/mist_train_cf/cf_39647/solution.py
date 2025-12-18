"""
QUESTION:
Implement the `balanced_bce_loss` function, which takes as input the predicted outputs, target labels, and the class weighting factor, and computes the balanced binary cross entropy loss for the given inputs.

Function Signature: `def balanced_bce_loss(outputs, targets, class_weight)`

Inputs: 
- `outputs`: list or array of floats representing the predicted outputs for the batch
- `targets`: list or array of integers representing the target labels for the batch (0 or 1)
- `class_weight`: float representing the class weighting factor

Output: 
- `loss`: float representing the computed balanced binary cross entropy loss for the given inputs

Assume inputs are valid and of the same length.
"""

import numpy as np

def balanced_bce_loss(outputs, targets, class_weight):
    epsilon = 1e-7  # Small value to avoid log(0) or log(1)
    
    # Compute the balanced binary cross entropy loss for each sample in the batch
    individual_losses = class_weight * targets * np.log(outputs + epsilon) + (1 - class_weight) * (1 - targets) * np.log(1 - outputs + epsilon)
    
    # Compute the mean loss over the batch
    loss = -np.mean(individual_losses)
    
    return loss