"""
QUESTION:
Implement a function named `find_median` that takes a list of integers as input and returns the median. The function must sort the input list in-place (without using extra space) and then calculate the median. The sorting process should be done using a sorting algorithm implemented from scratch, such as bubble sort or insertion sort, without using any built-in sorting functions.
"""

def find_median(arr):
    """
    Sorts the input list in-place using bubble sort and calculates the median.

    Args:
    arr (list): A list of integers.

    Returns:
    float: The median of the input list.
    """

    # Implement bubble sort to sort the input list in-place
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # Calculate the median
    if n % 2 == 0:
        # If the length is even, the median is the average of the two middle elements
        median = (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        # If the length is odd, the median is the middle element
        median = arr[n//2]

    return median