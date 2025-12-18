"""
QUESTION:
Write a function named `intersection` that takes two sorted arrays `arr1` and `arr2` as input and returns their intersection. The arrays are already sorted in ascending order. The function should return a new array containing the common elements of `arr1` and `arr2` in sorted order.
"""

def intersection(arr1, arr2):
    # Initialize two pointers in both arrays
    i, j = 0, 0
    # Initialize a list to store the intersection
    result = []

    # Iterate over both arrays and store the intersection
    while i < len(arr1) and j < len(arr2):
        # If both current elements are the same
        if arr1[i] == arr2[j]:
            # Store it in the result list and move both pointers
            result.append(arr1[i])
            i += 1
            j += 1
        # If the first array's current element is smaller
        elif arr1[i] < arr2[j]:
            i += 1
        # If the second array's current element is smaller
        else:
            j += 1

    # Return the result list
    return result