"""
QUESTION:
Create a function named `weighted_median` that takes a two-dimensional array `arr` as input, where each sub-array contains a number and its corresponding weight. The function should return the weighted median of the numbers in the array. The weighted median is the element that minimizes the sum of the absolute differences. The function should handle edge cases and return the weighted median.
"""

def weighted_median(arr):
    arr.sort()  # Sort the array by the elements
    weights = [x[1] for x in arr]  # Extract the weights
    elements = [x[0] for x in arr]  # Extract the elements
    # Compute the cumulative sum of the weights
    cumsum_weights = [sum(weights[:i+1]) for i in range(len(weights))]
    for i, weight in enumerate(cumsum_weights):
        # If the cumulative weight exceeds 0.5, the corresponding element is the weighted median
        if weight >= 0.5:
            return elements[i]