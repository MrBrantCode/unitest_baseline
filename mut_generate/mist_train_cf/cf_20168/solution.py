"""
QUESTION:
Write a function named `average_positive` that calculates the average of the positive integers in an array of n numbers. The function should have a time complexity of O(n) and a space complexity of O(1). If the array contains no positive integers, the function should return 0.
"""

def average_positive(arr):
    """
    Calculate the average of the positive integers in an array.

    Args:
        arr (list): A list of integers.

    Returns:
        float: The average of the positive integers in the array, or 0 if the array contains no positive integers.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    positive_sum = 0
    positive_count = 0

    for num in arr:
        if num > 0:
            positive_sum += num
            positive_count += 1

    if positive_count == 0:
        return 0  

    return positive_sum / positive_count