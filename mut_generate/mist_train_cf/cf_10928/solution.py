"""
QUESTION:
Write a function called `median_of_medians` that calculates the median of a given array using the median of medians algorithm. The array can contain duplicate elements and can have a length of up to 10^6, and the function should have a time complexity of O(nlogn) or better.
"""

def median_of_medians(arr):
    """
    Calculate the median of a given array using the median of medians algorithm.

    Args:
        arr (list): The input array.

    Returns:
        float: The median of the input array.
    """
    # Base case: If the array has one or zero elements, return the only element
    if len(arr) <= 1:
        return arr[0] if arr else None

    # Divide the array into subarrays of size 5
    subarrays = [arr[i:i+5] for i in range(0, len(arr), 5)]

    # Find the median of each subarray and store it in a new array
    medians = [sorted(subarray)[(len(subarray) - 1) // 2] for subarray in subarrays]

    # Recursively apply the algorithm to the medians array
    return median_of_medians(medians)