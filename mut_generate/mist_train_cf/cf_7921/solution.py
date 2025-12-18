"""
QUESTION:
Write a function `calculate_sum_and_median` that takes a list of mixed data types as input. The function should calculate the sum of all integers in the list and the median of these integers, ignoring non-integer values. If there are no integers in the list, the median should be null. The function should return the sum and median as output.
"""

def calculate_sum_and_median(lst):
    """
    Calculate the sum of all integers in the list and the median of these integers.

    Args:
    lst (list): A list of mixed data types.

    Returns:
    tuple: A tuple containing the sum of integers and their median.
    """
    
    # Filter out non-integer values
    integers = [x for x in lst if isinstance(x, int)]
    
    # Calculate the sum of integers
    total_sum = sum(integers)
    
    # If there are no integers in the list, return the sum and null for median
    if len(integers) == 0:
        return total_sum, None
    
    # Sort the integers in ascending order
    integers.sort()
    
    # Calculate the median
    n = len(integers)
    median = integers[n // 2] if n % 2 != 0 else (integers[n // 2 - 1] + integers[n // 2]) / 2
    
    return total_sum, median