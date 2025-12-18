"""
QUESTION:
Create a recursive function `count_divisible` that takes a list of numbers and a divisible number as input. The function should return the count of numbers in the list that are divisible by the given divisible number. The function should use recursion and have a default count parameter set to 0.
"""

def count_divisible(numbers, divisible_number, count=0):
    """
    Recursively count the numbers in the list that are divisible by the given divisible number.

    Args:
    numbers (list): A list of numbers.
    divisible_number (int): The number to check for divisibility.
    count (int, optional): The current count of divisible numbers. Defaults to 0.

    Returns:
    int: The count of numbers in the list that are divisible by the given divisible number.
    """
    if len(numbers) == 0:
        return count
    elif numbers[0] % divisible_number == 0:
        count += 1
    return count_divisible(numbers[1:], divisible_number, count)