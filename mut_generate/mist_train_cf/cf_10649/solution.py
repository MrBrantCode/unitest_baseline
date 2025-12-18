"""
QUESTION:
Write a function named `sum_elements_greater_than_or_equal_to_ten` that takes an array of integers as input and returns the sum of elements that are greater than or equal to 10. The function should not consider elements less than 10 in the calculation.
"""

def sum_elements_greater_than_or_equal_to_ten(arr):
    """
    This function calculates the sum of elements in an array that are greater than or equal to 10.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The sum of elements greater than or equal to 10.
    """
    total_sum = 0
    for num in arr:
        if num >= 10:
            total_sum += num
    return total_sum