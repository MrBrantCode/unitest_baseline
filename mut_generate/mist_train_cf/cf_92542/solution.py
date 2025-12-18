"""
QUESTION:
Write a function called `sum_of_skipped_elements` that calculates the sum of every second element in an array, where elements are skipped in a pattern of increasing consecutive skips (1, 2, 3, ..., then 1 again) until the end of the array is reached.
"""

def sum_of_skipped_elements(arr):
    """
    Calculate the sum of every second element in an array, 
    where elements are skipped in a pattern of increasing consecutive skips (1, 2, 3, ..., then 1 again) until the end of the array is reached.
    
    Args:
        arr (list): The input array.
    
    Returns:
        int: The sum of every second element based on the skipping pattern.
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