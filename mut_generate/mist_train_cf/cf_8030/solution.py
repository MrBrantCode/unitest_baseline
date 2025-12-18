"""
QUESTION:
Create a function `print_binomial_coefficients(n)` that takes an integer `n` as input, checks if it is a positive integer, and prints the binomial coefficients for each row from 0 to `n`. The function should handle large numbers efficiently with a time complexity of O(log(n)) or better.
"""

def print_binomial_coefficients(n):
    """
    This function prints the binomial coefficients for each row from 0 to n.
    
    Args:
        n (int): A positive integer.
    
    Returns:
        None
    """
    # Check if n is a positive integer
    if not isinstance(n, int) or n < 0:
        print("Error: Input must be a non-negative integer.")
        return
    
    # Initialize the first row
    row = [1]
    
    # Print the binomial coefficients for each row from 0 to n
    for i in range(n + 1):
        print(' '.join(map(str, row)))
        
        # Calculate the next row
        row = [x + y for x, y in zip([0] + row, row + [0])]