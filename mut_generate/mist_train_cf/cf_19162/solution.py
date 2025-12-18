"""
QUESTION:
Write a function `calculate_median` that takes a list of integers as input, sorts it in ascending order, and returns the median. The list can contain duplicate elements and has a maximum length of 100. The function should not use any built-in libraries or functions to calculate the median, and the time complexity should be O(nlogn).
"""

def calculate_median(dataset):
    # Sort the dataset in ascending order
    dataset.sort()
    
    # Check if the length of the dataset is even or odd
    length = len(dataset)
    if length % 2 == 1:  # Odd length
        return dataset[length // 2]
    else:  # Even length
        mid1 = dataset[length // 2 - 1]
        mid2 = dataset[length // 2]
        return (mid1 + mid2) / 2