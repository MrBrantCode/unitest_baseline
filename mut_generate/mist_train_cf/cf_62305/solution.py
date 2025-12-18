"""
QUESTION:
Write a function `exceeds_limit_sum` that determines whether the sum of any pair of numbers within a provided list surpasses a specified threshold. The function should take two parameters: a list of numbers and a limit. It should return `True` if any pair of numbers in the list sum to a value greater than the limit, and `False` otherwise.
"""

def exceeds_limit_sum(numbers, limit):
    """
    Determines whether the sum of any pair of numbers within a provided list surpasses a specified threshold.

    Args:
        numbers (list): A list of numbers.
        limit (float): The threshold value.

    Returns:
        bool: True if any pair of numbers in the list sum to a value greater than the limit, False otherwise.
    """
    numbers.sort()

    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] > limit:
            return True
        if numbers[left] + numbers[right] > limit:
            right -= 1
        else:
            left += 1
    return False