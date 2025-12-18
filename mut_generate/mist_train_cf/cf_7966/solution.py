"""
QUESTION:
Create a function `print_even_numbers(n)` that prints all even numbers from `n` down to 0 in descending order. The function should use recursion. The input `n` is an integer greater than or equal to 0.
"""

def print_even_numbers(n):
    """
    Prints all even numbers from n down to 0 in descending order using recursion.

    Args:
    n (int): An integer greater than or equal to 0.

    Returns:
    None
    """
    if n < 0:
        return
    if n % 2 == 0:
        print(n)
    print_even_numbers(n - 2)