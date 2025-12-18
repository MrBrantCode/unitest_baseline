"""
QUESTION:
Implement a function `compute_scalars(vector, target_sum)` that takes in a list of numbers `vector` and a number `target_sum` as input, and returns a list of numbers representing the scalar values αi such that the sum of the products αi*xi equals `target_sum`. The function should handle the case where the sum of the vector elements is zero and the target sum is not zero by raising an exception.
"""

def compute_scalars(vector, target_sum):
    # Compute the original sum of vector elements
    original_sum = sum(vector)
    
    # If the original sum is zero and the target sum is not zero, it's impossible to get the target sum
    if original_sum == 0 and target_sum != 0:
        raise Exception("It's impossible to get the target sum when the original sum is zero")

    # Compute the scale factor
    scale = target_sum / original_sum if original_sum > 0 else 0

    # Compute and return the scaled vector
    scalars = [scale * x for x in vector]
    return scalars