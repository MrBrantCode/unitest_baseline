"""
QUESTION:
Write a function `median_of_medians(arr, target_idx)` to calculate the median of an array `arr` using the efficient median of medians algorithm. The function should handle arrays with up to 10^6 elements, including duplicates, negative numbers, and floating-point numbers, with a time complexity of O(nlogn) or better. The array is 0-indexed, and `target_idx` represents the index of the median in the merged array. If the array length is even, the function should return the lower median.
"""

def median_of_medians(arr, target_idx):
    """
    Calculate the median of an array using the efficient median of medians algorithm.

    Args:
        arr (list): The input array.
        target_idx (int): The index of the median in the merged array.

    Returns:
        The median of the array.
    """

    # Base cases
    if len(arr) == 0:
        return None

    if len(arr) == 1:
        return arr[0]

    # Divide the array into subarrays of size 5
    subarrays = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    # Create a new array to store the medians of subarrays
    medians = []

    # For each subarray, sort it and find its median
    for subarray in subarrays:
        sorted_subarray = sorted(subarray)
        median_idx = len(sorted_subarray) // 2
        medians.append(sorted_subarray[median_idx])

    # Recursively call the median of medians algorithm on medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partition the original array around the pivot
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Calculate the length of each subarray
    smaller_len = len(smaller)
    equal_len = len(equal)
    greater_len = len(greater)

    # Recursively call the median of medians algorithm on the appropriate subarray
    if target_idx < smaller_len:
        return median_of_medians(smaller, target_idx)
    elif target_idx >= smaller_len + equal_len:
        return median_of_medians(greater, target_idx - smaller_len - equal_len)
    else:
        return pivot