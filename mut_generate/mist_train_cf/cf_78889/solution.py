"""
QUESTION:
Design a function called `find_narcissistic_numbers` that takes an integer `n` as input and returns all numbers less than or equal to `n` that are equal to the sum of their digits raised to the power of the number of digits.
"""

def find_narcissistic_numbers(n: int):
    """
    Returns all numbers less than or equal to `n` that are equal to the sum of their digits raised to the power of the number of digits.
    
    Args:
        n (int): The upper limit for the range of numbers to check.
    
    Returns:
        list: A list of narcissistic numbers less than or equal to `n`.
    """
    narcissistic_numbers = []
    for num in range(n + 1):
        num_str = str(num)
        power = len(num_str)
        sum_of_digits = sum(int(digit)**power for digit in num_str)
        if num == sum_of_digits:
            narcissistic_numbers.append(num)
    return narcissistic_numbers