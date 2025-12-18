"""
QUESTION:
Write a function `find_second_highest` that takes an array of integers as input and returns the second highest value in the array without using any built-in functions or libraries. The function should handle cases where there may not be a second highest value. If the array has less than two unique values, the function should return the lowest possible integer value.
"""

def find_second_highest(arr):
    """
    This function finds the second highest value in the given array.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The second highest value in the array. If the array has less than two unique values, returns negative infinity.
    """
    highest = float('-inf')
    second_highest = float('-inf')

    for num in arr:
        if num > highest:
            second_highest = highest
            highest = num
        elif num > second_highest and num != highest:
            second_highest = num

    return second_highest