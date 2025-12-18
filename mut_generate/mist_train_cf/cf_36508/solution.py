"""
QUESTION:
Implement a function `count_pattern_occurrences(dataset: array, pattern: array) -> int` that takes a 2D array dataset and a 2D pattern array, and returns the number of exact occurrences of the pattern within the dataset. The function should search for the pattern by sliding it over the dataset from left to right and from top to bottom. The dataset and pattern are represented as numpy arrays, and it is assumed that the pattern can fit entirely within the dataset.
"""

import numpy as np

def entance(dataset: np.array, pattern: np.array) -> int:
    dataset_height, dataset_width = dataset.shape
    pattern_height, pattern_width = pattern.shape
    count = 0

    for i in range(dataset_height - pattern_height + 1):
        for j in range(dataset_width - pattern_width + 1):
            if np.array_equal(dataset[i:i+pattern_height, j:j+pattern_width], pattern):
                count += 1

    return count