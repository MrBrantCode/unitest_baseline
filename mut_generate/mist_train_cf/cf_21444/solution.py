"""
QUESTION:
Write a function `sum_even_numbers` that takes a list of integers as input and returns the sum of the absolute values of all even numbers in the list. The function should have a time complexity of O(n) and space complexity of O(1), and should be able to handle large inputs with at least 10,000 elements and negative integers.
"""

def sum_even_numbers(numbers):
    """
    This function calculates the sum of the absolute values of all even numbers in a list.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        int: The sum of the absolute values of all even numbers in the list.
    """
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += abs(num)
    return even_sum