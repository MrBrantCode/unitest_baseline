"""
QUESTION:
Create a function `divisible_by_seven` that takes a list of numbers as input. Iterate through the list and return the sum of all numbers that are divisible by 7 and greater than 25, while excluding non-integer values. The function should also return the total count of such numbers.
"""

def divisible_by_seven(num_list):
    """
    This function calculates the sum of all numbers in a list that are divisible by 7 and greater than 25.
    It also returns the total count of such numbers, excluding non-integer values.

    Args:
        num_list (list): A list of numbers.

    Returns:
        tuple: A tuple containing the sum and count of numbers that meet the specified conditions.
    """
    divisible_count = 0
    divisible_sum = 0

    for num in num_list:
        try:
            if isinstance(num, int) and num % 7 == 0 and num > 25:
                divisible_count += 1
                divisible_sum += num
        except TypeError:
            pass

    return divisible_sum, divisible_count