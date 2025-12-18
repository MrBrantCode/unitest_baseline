"""
QUESTION:
Find the median of a given array of integers, rounded to the nearest integer. The array is not guaranteed to be sorted and can contain both even and odd number of elements. Implement a function called `find_median` that takes an array as input and returns the median value.
"""

def find_median(arr):
    """
    This function calculates the median of a given array of integers, rounded to the nearest integer.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The median value of the input array.
    """
    # First, sort the array in ascending order
    sorted_arr = sorted(arr)

    # Calculate the length of the array
    n = len(sorted_arr)

    # If the length of the array is odd, the median value is the middle element
    if n % 2 != 0:
        median = sorted_arr[n // 2]
    # If the length of the array is even, the median value is the average of the two middle elements
    else:
        median = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2

    # Return the median value rounded to the nearest integer
    return round(median)