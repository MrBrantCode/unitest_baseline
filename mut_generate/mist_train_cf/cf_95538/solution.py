"""
QUESTION:
Implement a function `calculate_median` that calculates the median of a given list of integers. The list can contain up to 100 elements, including duplicates. The function should have a time complexity of O(nlogn) and should not use any built-in libraries or functions to calculate the median.
"""

def calculate_median(dataset):
    dataset.sort()
    length = len(dataset)
    if length % 2 == 1:  # Odd length
        return dataset[length // 2]
    else:  # Even length
        mid1 = dataset[length // 2 - 1]
        mid2 = dataset[length // 2]
        return (mid1 + mid2) / 2