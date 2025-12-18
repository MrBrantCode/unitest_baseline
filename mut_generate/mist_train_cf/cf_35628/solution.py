"""
QUESTION:
Implement the `normalize_dataset` function to normalize a given dataset using the min-max scaling technique. The function should take a 2D numpy array as input and return a tuple containing the normalized dataset, the ranges for each feature, and the minimum values for each feature. The min-max scaling formula is `X_norm = (X - X_min) / (X_max - X_min)`, where `X_norm` is the normalized value, `X` is the original value, `X_min` is the minimum value of the feature, and `X_max` is the maximum value of the feature. The function should handle the calculation of `X_min` and `X_max` for each feature and perform the normalization.
"""

import numpy
from typing import Tuple

def normalize_dataset(dataset: numpy.ndarray) -> Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]:
    # Calculate the ranges and minimum values for each feature
    ranges = numpy.max(dataset, axis=0) - numpy.min(dataset, axis=0)
    min_values = numpy.min(dataset, axis=0)

    # Perform min-max scaling to normalize the dataset
    normalized_data = (dataset - min_values) / ranges

    return normalized_data, ranges, min_values