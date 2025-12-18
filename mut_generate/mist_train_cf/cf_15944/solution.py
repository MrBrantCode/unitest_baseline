"""
QUESTION:
Write a function called bubble_sort_custom that takes an array of integers as input and returns the array in descending order with all even numbers placed before odd numbers. The function should use the bubble sort algorithm.
"""

def bubble_sort_custom(arr):
    """
    This function takes an array of integers as input and returns the array in descending order with all even numbers placed before odd numbers.

    :param arr: A list of integers
    :return: A list of integers in descending order with all even numbers placed before odd numbers
    """
    # Rearrange the array in descending order using bubble sort
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # Ensure that all even numbers are placed before odd numbers
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] % 2 != 0 and arr[j + 1] % 2 == 0:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr