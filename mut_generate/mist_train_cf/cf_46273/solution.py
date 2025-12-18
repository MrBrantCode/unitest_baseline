"""
QUESTION:
Implement a function `multi_class_log_loss(labels, probabilities)` that calculates the multi-class logarithmic loss, assuming a logarithmic base of 'e'. The `labels` list contains 1-indexed class labels and the `probabilities` list contains the corresponding predicted class probabilities. The function should return the average multi-class logarithmic loss.
"""

import numpy as np

def multi_class_log_loss(labels, probabilities):
    n, m = len(labels), len(probabilities[0])
    y = np.zeros((n, m))
    y[np.arange(n), np.asarray(labels) - 1] = 1
    y_hat = np.asarray(probabilities)
    
    return -np.sum(y * np.log(y_hat)) / n