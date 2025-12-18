"""
QUESTION:
Create a function `merge_sorted_arrays(arr1, arr2)` that takes two sorted arrays as input and returns a new sorted array containing all elements from both arrays. The function should not use any built-in sorting functions and should have a time complexity of O(n), where n is the total number of elements in both arrays. No additional data structures or libraries can be used.
"""

def merge_sorted_arrays(arr1, arr2):
    # Initialize pointers for both arrays
    pointer1 = 0
    pointer2 = 0

    # Create an empty array to store the merged elements
    merged = []

    # Iterate until one of the arrays is exhausted
    while pointer1 < len(arr1) and pointer2 < len(arr2):
        # Compare the elements at the respective pointers
        if arr1[pointer1] <= arr2[pointer2]:
            merged.append(arr1[pointer1])
            pointer1 += 1
        else:
            merged.append(arr2[pointer2])
            pointer2 += 1

    # Add the remaining elements from the first array
    while pointer1 < len(arr1):
        merged.append(arr1[pointer1])
        pointer1 += 1

    # Add the remaining elements from the second array
    while pointer2 < len(arr2):
        merged.append(arr2[pointer2])
        pointer2 += 1

    return merged