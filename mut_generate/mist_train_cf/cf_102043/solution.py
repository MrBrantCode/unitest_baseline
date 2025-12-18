"""
QUESTION:
Write a function `find_divisible_numbers()` that takes a list of integers as input, and returns a tuple containing the sum and count of numbers in the list that are divisible by 3 and less than 100. The function should handle both positive and negative numbers.
"""

def find_divisible_numbers(numbers):
    """Returns a tuple containing the sum and count of numbers in the list that are divisible by 3 and less than 100."""
    divisible_numbers = [num for num in numbers if num % 3 == 0 and num < 100]
    sum_of_divisible_numbers = sum(divisible_numbers)
    count_of_divisible_numbers = len(divisible_numbers)
    
    return sum_of_divisible_numbers, count_of_divisible_numbers