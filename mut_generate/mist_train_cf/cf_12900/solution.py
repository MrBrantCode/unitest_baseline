"""
QUESTION:
Write a function `sum_every_second_element` that takes an array of integers as input and returns the sum of every second element in the array. The elements must be skipped in a specific pattern, starting by skipping 1 element, then 2 elements, then 3 elements, and so on, repeating the pattern until the end of the array is reached.
"""

def sum_every_second_element(arr):
    """
    This function calculates the sum of every second element in the input array,
    skipping elements in a pattern of increasing count (1, 2, 3, ...).
    
    Parameters:
    arr (list): The input list of integers.
    
    Returns:
    int: The sum of every second element in the array.
    """
    skip_count = 1  # Start by skipping 1 element
    sum_of_skipped_elements = 0  # Running sum of skipped elements

    for i in range(len(arr)):
        if skip_count > 0:
            skip_count -= 1
        else:
            sum_of_skipped_elements += arr[i]
            skip_count += 1

    return sum_of_skipped_elements