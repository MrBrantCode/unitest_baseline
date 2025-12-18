"""
QUESTION:
Write a Python function `calculate_median()` that takes a list of integers as input, sorts them in ascending order, and returns the median value. The input list can contain an odd or even number of integers. If the list has an even number of integers, the median is the average of the two middle numbers. If the list has an odd number of integers, the median is the middle number.
"""

def calculate_median(numbers):
    """
    This function calculates the median of a list of integers.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        float: The median value of the input list.
    """
    numbers.sort()
    len_numbers = len(numbers)

    if len_numbers % 2 == 0:  # even number of elements
        median1 = numbers[len_numbers//2]
        median2 = numbers[len_numbers//2 - 1]
        median = (median1 + median2)/2
    else:  # odd number of elements
        median = numbers[len_numbers//2]
    
    return median