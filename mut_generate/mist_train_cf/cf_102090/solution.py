"""
QUESTION:
Write a function called `find_second_largest_odd` that takes an array of integers as input and returns the index of the second largest odd value in the array. The function should handle arrays with both positive and negative numbers and possible duplicate values. If there is no second largest odd value (e.g., if there are no odd values or only one odd value), the function should return -1.
"""

def find_second_largest_odd(arr):
    """
    Returns the index of the second largest odd value in the array.
    If there is no second largest odd value, returns -1.

    :param arr: An array of integers.
    :return: The index of the second largest odd value, or -1 if not found.
    """
    largest_odd = float('-inf')
    second_largest_odd = float('-inf')
    largest_odd_index = -1
    second_largest_odd_index = -1

    for i, num in enumerate(arr):
        if num % 2 != 0:
            if num > largest_odd:
                second_largest_odd = largest_odd
                second_largest_odd_index = largest_odd_index
                largest_odd = num
                largest_odd_index = i
            elif num > second_largest_odd and num != largest_odd:
                second_largest_odd = num
                second_largest_odd_index = i

    return second_largest_odd_index