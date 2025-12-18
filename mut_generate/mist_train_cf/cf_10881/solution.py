"""
QUESTION:
Write a function called `flatten_and_remove_duplicates` that takes a 2D array of integers as input. The function should flatten the array while removing all duplicate elements and return the result in ascending order. The solution must have a time complexity of O(nlogn), where n is the total number of elements in the 2D array.
"""

def flatten_and_remove_duplicates(arr):
    # Flatten the 2D array
    flattened = []
    for row in arr:
        flattened.extend(row)

    # Sort the flattened list
    flattened.sort()

    # Create an empty result list
    result = []

    # Iterate through the sorted list
    for i in range(len(flattened)):
        # Remove duplicates and add elements to the result list
        if i == 0 or flattened[i] != flattened[i - 1]:
            result.append(flattened[i])

    # Return the result list
    return result