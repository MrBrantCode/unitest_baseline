"""
QUESTION:
Create a function named `calculate_statistics` that takes a list of integers as input. The function should sort the list in descending order, calculate the sum of all even numbers, and calculate the average of all odd numbers. The function should return the sum of even numbers and the average of odd numbers.
"""

def calculate_statistics(numbers):
    """
    This function takes a list of integers, sorts it in descending order, 
    calculates the sum of all even numbers, and calculates the average of all odd numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing the sum of even numbers and the average of odd numbers.
    """
    sorted_numbers = sorted(numbers, reverse=True)

    sum_even = 0
    odd_count = 0
    sum_odd = 0

    for num in sorted_numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
            odd_count += 1

    if odd_count == 0:
        average_odd = 0
    else:
        average_odd = sum_odd / odd_count

    return sum_even, average_odd