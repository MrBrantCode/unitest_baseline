"""
QUESTION:
Create a recursive function called `factorial_with_zeros(n)` that takes a single non-negative integer argument `n`. The function should return a string containing the factorial of `n` and the number of trailing zeros in the factorial result. If `n` is not a non-negative integer, the function should return an error message.
"""

def factorial_with_zeros(n):
    """
    Calculate the factorial of a number and the number of trailing zeros in the result.

    Args:
    n (int): A non-negative integer.

    Returns:
    str: A string containing the factorial of n and the number of trailing zeros in the result.
    """
    
    # Check if n is a valid input
    if type(n) != int or n < 0:
        return "Invalid input! Please enter a non-negative integer."

    # Calculate the factorial
    def calc_fact(n):
        return 1 if n == 0 else n * calc_fact(n - 1)

    fact = calc_fact(n)

    # Calculate the number of trailing zeros
    def count_zeros(n):
        count = 0
        i = 5
        while n / i >= 1:
            count += n // i
            i *= 5
        return count
    
    zeroes = count_zeros(n)

    return f"Factorial is: {fact}, Number of trailing zeroes is: {zeroes}"