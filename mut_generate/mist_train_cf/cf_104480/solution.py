"""
QUESTION:
Write a function named `sum_even_divisible_by_four` that calculates the total sum of all even numbers that are divisible by 4 in a given list of integers. The function should use an accumulator pattern and return the calculated sum. The input list can contain both positive and negative integers.
"""

def sum_even_divisible_by_four(numbers):
    """
    Calculate the total sum of all even numbers that are divisible by 4 in a given list of integers.
    
    Args:
    numbers (list): A list of integers.
    
    Returns:
    int: The total sum of all even numbers that are divisible by 4 in the given list.
    """
    total_sum = 0
    for num in numbers:
        if num % 2 == 0 and num % 4 == 0:
            total_sum += num
    return total_sum