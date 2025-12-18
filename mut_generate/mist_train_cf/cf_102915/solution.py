"""
QUESTION:
Write a function `calculate_odd_average` that calculates the sum and average of all odd elements in a given list. The function should not use any built-in functions for calculating the sum or average, and it should not use the modulus operator (%) to check if a number is odd. The function should return a tuple containing the sum and average of the odd elements. If the list does not contain any odd elements, the function should return a sum of 0 and an average of 0.
"""

def calculate_odd_average(nums):
    """
    Calculates the sum and average of all odd elements in a given list.

    Args:
        nums (list): A list of integers.

    Returns:
        tuple: A tuple containing the sum and average of the odd elements.
    """
    odd_sum = 0
    odd_count = 0

    for num in nums:
        # Use bitwise AND operator with 1 to check if the number is odd
        odd_sum = odd_sum + (num & 1) * num
        odd_count = odd_count + (num & 1)  # increment odd_count if the number is odd

    if odd_count > 0:
        odd_average = odd_sum / odd_count
    else:
        odd_average = 0

    return odd_sum, odd_average