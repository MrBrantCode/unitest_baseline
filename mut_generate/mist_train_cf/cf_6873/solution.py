"""
QUESTION:
Write a function `sum_even_numbers` that takes a list of integers as input and returns the sum of the absolute values of all even numbers in the list. The function should have a time complexity of O(n) and space complexity of O(1) to handle large inputs efficiently.
"""

def sum_even_numbers(numbers):
    """
    This function calculates the sum of the absolute values of all even numbers in a given list.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of the absolute values of all even numbers in the list.
    """
    def recursive_sum(numbers, index=0):
        # Base case: If the index is out of range, return 0
        if index == len(numbers):
            return 0
        # If the current number is even, add its absolute value to the sum
        elif numbers[index] % 2 == 0:
            return abs(numbers[index]) + recursive_sum(numbers, index + 1)
        # If the current number is odd, skip it and move to the next number
        else:
            return recursive_sum(numbers, index + 1)

    return recursive_sum(numbers)