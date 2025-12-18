"""
QUESTION:
Write a function `sum_and_count_divisible_by_three` that takes an array of integers as input, calculates the sum of numbers that are divisible by 3 and not divisible by 5, and returns a tuple containing the sum and the count of such numbers.
"""

def sum_and_count_divisible_by_three(nums):
    """
    This function calculates the sum of numbers in the input array that are divisible by 3 and not divisible by 5,
    and returns a tuple containing the sum and the count of such numbers.

    Args:
        nums (list): A list of integers.

    Returns:
        tuple: A tuple containing the sum and the count of numbers that are divisible by 3 and not divisible by 5.
    """

    sum_nums = 0
    count_nums = 0

    for num in nums:
        if num % 3 == 0 and num % 5 != 0:
            sum_nums += num
            count_nums += 1

    return (sum_nums, count_nums)