"""
QUESTION:
Implement the function sum_divisible_by_2_greater_than_5 that takes a list of integers as input and returns the sum of all elements that are divisible by 2 and greater than 5, excluding any elements that are divisible by both 3 and 4. The solution must use recursion, not loops, and should not modify the original list. The function should handle empty lists.
"""

def sum_divisible_by_2_greater_than_5(numbers):
    """
    This function calculates the sum of all elements in a list that are divisible by 2 and greater than 5,
    excluding any elements that are divisible by both 3 and 4.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of the elements that meet the specified conditions.
    """
    if len(numbers) == 0:
        return 0
    elif numbers[0] % 2 == 0 and numbers[0] > 5 and (numbers[0] % 3 != 0 or numbers[0] % 4 != 0):
        return numbers[0] + sum_divisible_by_2_greater_than_5(numbers[1:])
    else:
        return sum_divisible_by_2_greater_than_5(numbers[1:])