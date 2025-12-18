"""
QUESTION:
Implement a function named `normalize_vector` that takes a list of floats representing a vector and returns its normalized version by dividing each element by the vector's Euclidean norm (magnitude). The function should be able to handle vectors of any dimension.

The function should have the following signature: `def normalize_vector(u: List[float]) -> List[float]`.
"""

from typing import List
import numpy as np

def normalize_vector(u: List[float]) -> List[float]:
    magnitude = np.sqrt(sum([x ** 2 for x in u]))  # Calculate the magnitude of the vector
    normalized_u = [x / magnitude for x in u]  # Normalize each element of the vector
    return normalized_u