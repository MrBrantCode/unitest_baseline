"""
QUESTION:
Write a function named `sum_even_numbers` that calculates the sum of all even integers from 1 to the given number n. The function should take one argument: an integer n. The function should return the sum of all even integers from 1 to n (inclusive). The input n can be any non-negative integer.
"""

def sum_even_numbers(n):
    """
    This function calculates the sum of all even integers from 1 to the given number n.
    
    Args:
    n (int): The input number up to which the sum of even integers is calculated.
    
    Returns:
    int: The sum of all even integers from 1 to n (inclusive).
    """
    
    # Calculate the number of even integers between 1 and n
    num_even_integers = n // 2
    
    # Calculate the last even integer
    if n % 2 == 0:
        last_even_integer = n
    else:
        last_even_integer = n - 1
    
    # Calculate the sum of even integers using the formula for the sum of an arithmetic series
    sum_even_integers = (num_even_integers) * (2 + last_even_integer)
    
    return sum_even_integers