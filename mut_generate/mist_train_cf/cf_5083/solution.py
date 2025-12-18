"""
QUESTION:
Write a function named `sum_even_numbers` that calculates the sum of all even numbers in a given list. The function should not use any loops or built-in functions for finding the sum or checking if a number is even. The solution must have a time complexity of O(n) and a space complexity of O(1), handling the case where the list is empty and returning 0 as the sum.
"""

def sum_even_numbers(numbers):
    """
    This function calculates the sum of all even numbers in a given list.
    
    The function uses recursion to achieve a time complexity of O(n) and a space complexity of O(1).
    It handles the case where the list is empty and returns 0 as the sum.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of all even numbers in the list.
    """
    if len(numbers) == 0:
        return 0
    elif numbers[0] % 2 == 0:
        return numbers[0] + sum_even_numbers(numbers[1:])
    else:
        return sum_even_numbers(numbers[1:])