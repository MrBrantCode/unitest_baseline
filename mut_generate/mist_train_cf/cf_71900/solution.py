"""
QUESTION:
Write a function `reorder_calculate_difference` that takes an array of integers as input and returns two values: a reordered array where all negative integers appear before all positive integers (while preserving the order of negative and positive integers within their respective groups), and the difference between the sum of all positive integers and the absolute sum of all negative integers in the array.
"""

def reorder_calculate_difference(arr):
    """
    Reorders an array of integers so that all negative integers appear before all positive integers, 
    and calculates the difference between the sum of all positive integers and the absolute sum of all negative integers.

    Args:
        arr (list): A list of integers.

    Returns:
        tuple: A reordered list and the difference between the sum of positive integers and the absolute sum of negative integers.
    """

    # Separate positive and negative numbers into different lists
    positive = [num for num in arr if num >= 0]
    negative = [num for num in arr if num < 0]

    # Concatenate negative and positive numbers to get the reordered array
    reordered_array = negative + positive

    # Calculate the difference between sum of positive and absolute sum of negative numbers
    difference = sum(positive) - sum(abs(num) for num in negative)

    return reordered_array, difference