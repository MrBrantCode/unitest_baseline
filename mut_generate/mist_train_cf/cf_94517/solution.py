"""
QUESTION:
Implement the function `sum_and_average_odd_elements(lst)` to calculate the average of all odd elements in a list using a for loop. The function should not use any built-in functions for calculating the sum or average of elements in the list and should not use the modulus operator (%) to check if a number is odd. If the list contains no odd elements, the function should return 0.
"""

def sum_and_average_odd_elements(lst):
    """
    Calculate the average of all odd elements in a list using a for loop.

    Args:
        lst (list): A list of integers.

    Returns:
        float: The average of all odd elements in the list. If the list contains no odd elements, returns 0.
    """
    odd_sum = 0
    odd_count = 0

    for num in lst:
        odd_sum += num * (num & 1)  # multiply by 1 if odd, 0 if even
        odd_count += num & 1  # count 1 if odd, 0 if even

    average = odd_sum / odd_count if odd_count != 0 else 0
    return average