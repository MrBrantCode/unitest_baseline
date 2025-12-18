"""
QUESTION:
Implement a function `calculate_entropy(data: Union[str, bytes]) -> float` that calculates the entropy of a given text or binary data. The function should return the calculated entropy value using the Shannon entropy formula for text data and the binary entropy formula for binary data, handling empty input, text data, and binary data cases.
"""

from typing import Union
import math

def calculate_entropy(data: Union[str, bytes]) -> float:
    if not data:
        return 0.0  # Return 0.0 for empty input

    if isinstance(data, str):  # Calculate entropy for text data
        probabilities = [float(data.count(c)) / len(data) for c in set(data)]
        entropy = -sum(p * math.log2(p) for p in probabilities)
    else:  # Calculate entropy for binary data
        ones = data.count(b'\x01')
        total_bits = len(data) * 8  # Assuming 8 bits per byte
        p = ones / total_bits
        entropy = -p * math.log2(p) - (1 - p) * math.log2(1 - p)

    return entropy