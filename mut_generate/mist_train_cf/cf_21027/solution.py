"""
QUESTION:
Write a function `find_largest` that takes an array of integers as input and returns the largest number in the array. The array can contain both positive and negative integers. Your solution must not use any built-in functions or methods and should only utilize basic arithmetic operations and control structures. Additionally, the time complexity of your solution should be O(n), where n is the length of the array.
"""

def find_largest(array):
    """
    This function finds the largest number in an array of integers.

    Args:
        array (list): A list of integers.

    Returns:
        int: The largest number in the array.
    """
    max_num = array[0]  # Assume the first number is the maximum

    for num in array:
        if num > max_num:
            max_num = num

    return max_num