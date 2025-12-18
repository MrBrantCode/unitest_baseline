"""
QUESTION:
Write a function named findMiddle that takes a sorted list of integers as input and returns the middle element. If the list has an even number of elements, the function should return the average of the two middle elements.
"""

def findMiddle(arr):
    """
    This function takes a sorted list of integers as input and returns the middle element.
    If the list has an even number of elements, the function returns the average of the two middle elements.

    Parameters:
    arr (list): A sorted list of integers.

    Returns:
    int or float: The middle element or the average of the two middle elements.
    """
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2] + arr[n//2 - 1]) / 2
    else:
        return arr[n//2]