"""
QUESTION:
Write a function `starts_one_ends(n)` that calculates the number of n-digit positive integers that start or end with the digit 1. The function takes a positive integer `n` as input and returns the total count. Note that the function should handle the case when `n` is 1 separately.
"""

def starts_one_ends(n):
    """
    Calculate the number of n-digit positive integers that start or end with the digit 1.

    Args:
        n (int): The number of digits.

    Returns:
        int: The total count of n-digit positive integers that start or end with the digit 1.
    """
    
    # if n is 1, then there're 2 numbers start or end with 1, which are 1 itself 
    if n == 1:
        return 2
    
    # if n is greater than 1, for each n digit number that starts or ends with 1
    # there're 10^(n-1) possible n-digit numbers starting with 1 
    # and 9 * 10^(n-2) possible n-digit numbers ending with 1 (excluding numbers starting with 1)
    # so total numbers = 10^(n-1) + 9 * 10^(n-2)
    else:  
        total_numbers = 10 ** (n-1) + 9 * 10 ** (n-2)
        
        return total_numbers