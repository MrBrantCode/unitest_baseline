"""
QUESTION:
Create a function called `sum_odd_excluding_multiples_of_three` that calculates the sum of all odd numbers between 1 and a given number n (inclusive), excluding any numbers that are multiples of 3.
"""

def sum_odd_excluding_multiples_of_three(n):
    """
    Calculate the sum of all odd numbers between 1 and n (inclusive), 
    excluding any numbers that are multiples of 3.

    Args:
        n (int): The upper limit (inclusive).

    Returns:
        int: The sum of all odd numbers excluding multiples of 3.
    """
    return sum(num for num in range(1, n+1) if num % 2 != 0 and num % 3 != 0)