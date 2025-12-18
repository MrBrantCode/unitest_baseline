"""
QUESTION:
Write a function `sum_three_elements(array, number)` that takes an array of integers and a target number as input. The function should return True if there exist three elements in the array whose sum is equal to the given number, and False otherwise. The array may contain duplicate numbers and is not guaranteed to be sorted. The function should have a time complexity of O(n^2) or better.
"""

def sum_three_elements(array, number):
    """
    Given an array with n numbers, find if there exists three elements in the array whose sum is equal to a given number.

    Args:
    array (list): A list of integers.
    number (int): The target number.

    Returns:
    bool: True if three elements in the array sum up to the target number, False otherwise.
    """
    array.sort()
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            temp = array[i] + array[left] + array[right]
            if temp == number:
                return True
            elif temp < number:
                left += 1
            else:
                right -= 1
    return False