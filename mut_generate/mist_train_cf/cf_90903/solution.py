"""
QUESTION:
Write a function `find_median(arr)` that finds the median of a sorted array in O(log n) time. The input array `arr` is sorted in ascending order. If the array has an even number of elements, the median is the average of the two middle elements; if the array has an odd number of elements, the median is the middle element. The function should return the calculated median.
"""

def find_median(arr):
    """
    Finds the median of a sorted array in O(log n) time.

    Args:
    arr (list): A sorted list of numbers in ascending order.

    Returns:
    float: The calculated median.
    """
    n = len(arr)
    
    if n % 2 == 0:  # If the array has even length
        mid = n // 2
        median = (arr[mid] + arr[mid - 1]) / 2
    else:  # If the array has odd length
        mid = n // 2
        median = arr[mid]
    
    return median