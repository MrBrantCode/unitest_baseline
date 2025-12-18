"""
QUESTION:
Write a function named `exclude_divisible_by_3_and_contains_7` that takes a list of integers as input, filters out the numbers that are divisible by 3 or contain the digit '7', and returns the remaining numbers in ascending order. Additionally, calculate the average of the remaining numbers and round it to two decimal places.
"""

def exclude_divisible_by_3_and_contains_7(numbers):
    """
    This function takes a list of integers as input, filters out the numbers that are divisible by 3 or contain the digit '7', 
    and returns the remaining numbers in ascending order along with their average rounded to two decimal places.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing the filtered list of numbers in ascending order and their average.
    """
    filtered_numbers = sorted([num for num in numbers if num % 3 != 0 and '7' not in str(num)])
    average = round(sum(filtered_numbers) / len(filtered_numbers), 2) if filtered_numbers else 0
    return filtered_numbers, average