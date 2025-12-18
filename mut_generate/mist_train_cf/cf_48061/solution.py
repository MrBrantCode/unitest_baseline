"""
QUESTION:
Develop a recursive function named `factorial` that takes two parameters: an integer `n` and a mutable list `counts` containing a single integer to track the number of recursive calls. The function should return the factorial of `n` and update the `counts` list with the total number of recursive calls made. Ensure that the function correctly handles the base case where `n` is 0 or 1.
"""

def factorial(n, counts):
    """
    Calculating factorial using recursive approach
    
    Args:
    n : integer
        the number for factorial calculation
    counts : Counter
        counter to count the number of recursive calls
        
    Returns:
    n! : integer
        factorial of n
    """
    
    # increment the counter
    counts[0] += 1
    
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n - 1, counts)