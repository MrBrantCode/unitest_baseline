"""
QUESTION:
Write a function `weighted_average` that calculates the weighted average of a list of integers. The function should exclude any negative numbers and numbers divisible by 3 from the calculation. The weight of each number is determined by its index in the list, starting with 1. If all numbers in the list are excluded, the function should return 0.
"""

def weighted_average(numbers):
    """
    Calculates the weighted average of a list of integers, excluding negative numbers and numbers divisible by 3.
    
    The weight of each number is determined by its index in the list, starting with 1.
    If all numbers in the list are excluded, the function returns 0.

    Args:
        numbers (list): A list of integers.

    Returns:
        float: The weighted average of the list.
    """
    total = 0
    weight = 0
    for i, num in enumerate(numbers, start=1):
        if num < 0 or num % 3 == 0:
            continue
        weight += 1
        total += num * i
    if weight == 0:
        return 0
    return total / weight