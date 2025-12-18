"""
QUESTION:
Calculate the sum of elements in an array where elements are selected by skipping an increasing number of elements. The skipping pattern starts by skipping 2 elements, then 3 elements, then 4 elements, and so on. Write a function called `calculate_sum` that takes an array of integers as input and returns the calculated sum. The function should be able to handle arrays of any length.
"""

def calculate_sum(arr):
    """
    Calculate the sum of elements in an array where elements are selected by skipping an increasing number of elements.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The calculated sum.
    """
    skip = 2
    total_sum = 0
    index = 0

    while index < len(arr):
        total_sum += arr[index]
        index += skip + 1
        skip += 1

    return total_sum