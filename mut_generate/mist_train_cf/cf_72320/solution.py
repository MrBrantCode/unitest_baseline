"""
QUESTION:
Write a function called `count_palindromes(n, divisor)` that takes two parameters: the upper limit `n` and a prime number `divisor`, and returns an approximation of the quantity of palindromic numbers that fall under `n` and are divisible by `divisor`. Assume the distribution of palindromic numbers is uniform.
"""

def count_palindromes(n, divisor):
    """
    Returns an approximation of the quantity of palindromic numbers that fall under `n` and are divisible by `divisor`.
    
    Parameters:
    n (int): The upper limit
    divisor (int): A prime number
    
    Returns:
    int: An approximation of the quantity of palindromic numbers that fall under `n` and are divisible by `divisor`
    """
    # Calculate the number of digits in n
    num_digits = len(str(n))
    
    # For even number of digits, we have (num_digits / 2) pairs of digits to fill
    # For odd number of digits, we have (num_digits // 2) pairs of digits and one middle digit
    # We assume the distribution of palindromic numbers is uniform
    num_palindromes = 2 * (10 ** (num_digits // 2))
    
    # Return an approximation of the quantity of palindromic numbers that fall under `n` and are divisible by `divisor`
    return num_palindromes // divisor