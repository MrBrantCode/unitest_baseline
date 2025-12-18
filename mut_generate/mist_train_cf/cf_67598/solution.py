"""
QUESTION:
Create a function `flatten_and_sort_3D_array` that takes a 3D array as input, reorders the layers in ascending order based on the sum of their elements (after removing negative values), removes negative values from each layer, and returns the flattened 1D array. The input 3D array has p layers, each with m horizontal lines and n vertical lines. The function should have an optimized time complexity.
"""

def flatten_and_sort_3D_array(array):
    # Remove negative numbers and calculate the sum for each layer
    layers_sum = []
    for i, layer in enumerate(array):
        layer_sum = sum(j for x in layer for j in x if j >= 0)
        removed_neg_values = [[j for j in x if j >= 0] for x in layer]
        layers_sum.append((layer_sum, removed_neg_values))

    # Sort the layers based on their sum
    layers_sum.sort()

    # Flatten the layers
    flat_array = [j for i in layers_sum for x in i[1] for j in x]

    return flat_array