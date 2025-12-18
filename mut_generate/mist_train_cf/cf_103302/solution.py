"""
QUESTION:
Write a function named find_median to calculate the median of a given array of integers. The array may have an odd or even number of elements. If the array has an odd number of elements, the median is the middle element. If the array has an even number of elements, the median is the average of the two middle elements. The array should be sorted in ascending order before calculating the median.
"""

def find_median(arr):
    """
    Calculate the median of a given array of integers.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        float: The median of the array.
    """
    # Sort the array in ascending order
    arr.sort()
    
    # Calculate the median
    n = len(arr)
    if n % 2 == 0:
        # If the array has an even number of elements, 
        # the median is the average of the two middle elements
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        # If the array has an odd number of elements, 
        # the median is the middle element
        median = arr[n // 2]
    
    return median