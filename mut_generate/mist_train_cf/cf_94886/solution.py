"""
QUESTION:
Implement a function `bubble_sort` that sorts an array of integers in ascending order using bubble sort and then finds the median. The function should sort the array in-place without using any extra space or built-in sorting functions. The function should return the sorted array and its median. If the array length is odd, the median is the middle element; if the length is even, the median is the average of the two middle elements.
"""

def bubble_sort(arr):
    """
    Sorts an array of integers in ascending order using bubble sort and returns the sorted array and its median.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The sorted array and its median.
    """

    n = len(arr)
    
    # Bubble sort algorithm
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # Calculate median
    if n % 2 == 0:
        median = (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        median = arr[n//2]

    return arr, median