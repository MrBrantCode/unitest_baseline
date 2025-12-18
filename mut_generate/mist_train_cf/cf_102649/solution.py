"""
QUESTION:
Write a function `softmax_top_k` that takes a list of numbers `nums` and an integer `k` as input, applies the softmax function to `nums`, sorts the resulting probabilities in descending order, and returns the sum of the top `k` probabilities.
"""

import numpy as np

def softmax_top_k(nums, k):
    softmax_probs = np.exp(nums) / np.sum(np.exp(nums))
    top_k_indices = np.argsort(softmax_probs)[::-1][:k]
    top_k_probs = softmax_probs[top_k_indices]
    return np.sum(top_k_probs)