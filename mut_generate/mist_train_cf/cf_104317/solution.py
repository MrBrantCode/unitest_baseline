"""
QUESTION:
Write a function `sum_filtered_numbers` that takes a list of integers as input, and returns the sum of the numbers that are greater than 2, divisible by 2, and have a digit sum that is a multiple of 3. The input list is guaranteed to be sorted in descending order.
"""

def sum_filtered_numbers(numbers):
    """
    This function calculates the sum of numbers in a list that are greater than 2, 
    divisible by 2, and have a digit sum that is a multiple of 3.
    
    Parameters:
    numbers (list): A list of integers in descending order.
    
    Returns:
    int: The sum of the filtered numbers.
    """
    return sum(num for num in numbers if num > 2 and num % 2 == 0 and sum([int(digit) for digit in str(num)]) % 3 == 0)