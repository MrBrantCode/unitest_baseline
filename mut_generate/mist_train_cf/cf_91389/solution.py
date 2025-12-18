"""
QUESTION:
Create a function `generate_even_numbers` that generates a list of even numbers within a specified range from 1 to n (inclusive). The function should return a list of integers where each integer is an even number in the range.
"""

def generate_even_numbers(n):
    """
    Generates a list of even numbers within a specified range from 1 to n (inclusive).

    Args:
        n (int): The upper limit of the range (inclusive).

    Returns:
        list: A list of even numbers in the range.
    """
    even_numbers = [i for i in range(1, n + 1) if i % 2 == 0]
    return even_numbers