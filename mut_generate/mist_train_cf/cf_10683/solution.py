"""
QUESTION:
Write a function `process_numbers` that takes a list of numbers as input, iterates over it, and returns a string of comma-separated squares of the numbers that are integers, divisible by 2, and less than 10. The function should also return the sum of these squared numbers. The function should handle non-integer inputs.
"""

def process_numbers(numbers):
    """
    This function takes a list of numbers, squares the numbers that are integers, 
    divisible by 2, and less than 10, then returns these squared numbers as a 
    string and their sum.

    Args:
        numbers (list): A list of numbers.

    Returns:
        tuple: A tuple containing a string of comma-separated squared numbers 
        and their sum.
    """
    squared_nums = [num ** 2 for num in numbers if isinstance(num, int) and num % 2 == 0 and num < 10]
    squared_nums_str = ", ".join(str(num) for num in squared_nums)
    sum_of_squares = sum(squared_nums)
    
    return squared_nums_str, sum_of_squares