"""
QUESTION:
Create a function named `exclude_divisible_by_3_and_contains_7` that takes a list of integers as input, and returns a new list containing the input numbers that are not divisible by 3 and do not contain the digit '7'. The returned list should be in ascending order and include duplicate numbers if present in the input list. Additionally, calculate the average of the returned numbers and return it as a decimal rounded to two decimal places.
"""

def exclude_divisible_by_3_and_contains_7(numbers):
    """
    Returns a list of numbers that are not divisible by 3 and do not contain the digit '7'.
    The returned list is in ascending order and includes duplicate numbers if present in the input list.
    The average of the returned numbers is also calculated and returned as a decimal rounded to two decimal places.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing the filtered list and the average of the filtered numbers.
    """
    filtered_numbers = [num for num in numbers if num % 3 != 0 and '7' not in str(num)]
    average = round(sum(filtered_numbers) / len(filtered_numbers), 2) if filtered_numbers else 0.0
    return sorted(filtered_numbers), average