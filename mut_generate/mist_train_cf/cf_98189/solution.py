"""
QUESTION:
Write a function `sum_even_numbers` that takes an integer array as input and returns the sum of all even elements using the `SimpleArrayAddition` object, without modifying the original array.
"""

def sum_even_numbers(arr):
    """
    :param arr: a list of integers
    :return: the sum of all the even elements in the list
    """
    sum = 0
    for num in arr:
        if num % 2 == 0:
            sum += num
    return sum