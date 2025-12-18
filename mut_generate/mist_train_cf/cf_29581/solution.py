"""
QUESTION:
Implement a custom Negative Log-Likelihood (NLL) loss function named `custom_nll_loss` that takes two inputs: 

- `predicted_probs`: A 2D NumPy array of shape (batch_size, num_classes) containing the predicted class probabilities for each sample in the batch.
- `true_labels`: A 1D NumPy array of shape (batch_size) containing the true class labels for each sample in the batch.

The function should return two outputs: 

- `nll_loss`: A scalar NumPy float representing the computed NLL loss for the batch.
- `grad_predicted_probs`: A 2D NumPy array of the same shape as `predicted_probs` containing the gradient of the NLL loss with respect to the predicted class probabilities.

The function should compute the NLL loss and its gradient for each sample in the batch and then average them over the batch.
"""

import numpy as np

def custom_nll_loss(predicted_probs, true_labels):
    batch_size = predicted_probs.shape[0]
    nll_loss = 0.0
    grad_predicted_probs = np.zeros_like(predicted_probs)

    for i in range(batch_size):
        true_label = true_labels[i]
        probs = predicted_probs[i]
        nll_loss -= np.log(probs[true_label])
        grad_predicted_probs[i] = -1 / probs
        grad_predicted_probs[i, true_label] += 1 / probs[true_label]

    nll_loss /= batch_size
    grad_predicted_probs /= batch_size

    return nll_loss, grad_predicted_probs