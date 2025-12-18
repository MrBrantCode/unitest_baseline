"""
QUESTION:
Write a function named `sum_even_elements` that calculates the sum of even elements in a list of positive integers, excluding any element greater than 10. The function should have a time complexity of O(n) and should not use any built-in sum or filter functions. The space complexity should be O(1) or as low as possible.
"""

def sum_even_elements(lst):
    """
    Calculate the sum of even elements in a list of positive integers, 
    excluding any element greater than 10.

    Args:
        lst (list): A list of positive integers.

    Returns:
        int: The sum of even elements not greater than 10.
    """
    total_sum = 0
    for num in lst:
        if num % 2 == 0 and num <= 10:
            total_sum += num
    return total_sum