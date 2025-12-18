"""
QUESTION:
Implement the `softmax_loss` function, which calculates the softmax loss and its gradient with respect to the input scores. The function takes two inputs: `x`, a 2D array of shape (N, C) where `x[i, j]` is the score for the jth class for the ith input, and `y`, a 1D array of shape (N,) where `y[i]` is the label for `x[i]` and `0 <= y[i] < C`. The function should return a tuple containing the scalar loss and the gradient of the loss with respect to `x`, which is a 2D array of shape (N, C).
"""

import numpy as np

def softmax_loss(x, y):
    """
    Computes the softmax loss and its gradient with respect to the input scores.

    Inputs:
    - x: Input scores, of shape (N, C) where x[i, j] is the score for the jth class
         for the ith input.
    - y: Vector of labels, of shape (N,) where y[i] is the label for x[i] and
         0 <= y[i] < C

    Returns a tuple of:
    - loss: Scalar giving the loss
    - dx: Gradient of the loss with respect to x
    """
    N = x.shape[0]
    exp_scores = np.exp(x - np.max(x, axis=1, keepdims=True))
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    correct_logprobs = -np.log(probs[range(N), y])
    loss = np.sum(correct_logprobs) / N

    dx = probs.copy()
    dx[range(N), y] -= 1
    dx /= N

    return loss, dx