"""
QUESTION:
Write a function `findMinPositiveOdd` that takes an array of integers as input and returns the minimum positive odd number in the array. The integers in the array are in the range -100 to 100. If there are no positive odd numbers in the array, the function should return -1.
"""

def findMinPositiveOdd(arr):
    """
    This function takes an array of integers as input and returns the minimum positive odd number in the array.
    If there are no positive odd numbers in the array, the function returns -1.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The minimum positive odd number in the array, or -1 if no such number exists.
    """
    min_odd = float('inf')
    for num in arr:
        if num > 0 and num % 2 != 0:
            min_odd = min(min_odd, num)
    return min_odd if min_odd != float('inf') else -1