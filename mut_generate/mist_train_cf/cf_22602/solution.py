"""
QUESTION:
Create a function `mergeArrays(arr1, arr2)` that merges two sorted arrays `arr1` and `arr2` into a new sorted array. The input arrays will be sorted in ascending order, contain elements that can be positive, negative, or zero, and have sizes ranging from 0 to 10^6. The function should have a time complexity of O(n + m), where n and m are the sizes of the input arrays, and should not use any additional data structures or allocate additional space.
"""

def mergeArrays(arr1, arr2):
    """
    Merge two sorted arrays into a new sorted array.

    Args:
        arr1 (list): The first sorted array.
        arr2 (list): The second sorted array.

    Returns:
        list: A new sorted array containing all elements from arr1 and arr2.

    Time Complexity:
        O(n + m), where n and m are the sizes of arr1 and arr2, respectively.

    Space Complexity:
        O(n + m), for the merged array.
    """

    # Initialize an empty list to store the merged array
    merged = []

    # Get the lengths of the input arrays
    n = len(arr1)
    m = len(arr2)

    # Initialize two pointers for the input arrays
    i = 0
    j = 0

    # Merge smaller elements first
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            # If arr1[i] is smaller, append it to the merged array and increment i
            merged.append(arr1[i])
            i += 1
        else:
            # If arr2[j] is smaller, append it to the merged array and increment j
            merged.append(arr2[j])
            j += 1

    # Append any remaining elements from arr1
    while i < n:
        merged.append(arr1[i])
        i += 1

    # Append any remaining elements from arr2
    while j < m:
        merged.append(arr2[j])
        j += 1

    # Return the merged array
    return merged