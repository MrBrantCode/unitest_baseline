"""
QUESTION:
Create a function `arraySort(elements, weights)` that takes two lists of integers as input, `elements` and `weights`, and returns a list of integers sorted based on their corresponding weights and values. The length of `elements` is greater than or equal to the length of `weights`. If an element in `elements` does not have a corresponding weight in `weights`, consider its weight as zero. Sort the elements primarily by their weights in descending order and secondarily by their values in descending order.
"""

def arraySort(elements, weights):
    # If elements without weight, assign zero weight
    weights += [0] * (len(elements) - len(weights))

    # Pair each element with its weight
    pairing = list(zip(elements, weights))

    # Sort primarily by weight and secondarily by value, both in descending order
    pairing.sort(key=lambda x: (x[1], x[0]), reverse=True)

    # Select only the element from each pair
    return [pair[0] for pair in pairing]