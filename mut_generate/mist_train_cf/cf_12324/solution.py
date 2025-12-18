"""
QUESTION:
Write a function `sum_of_digits(N)` that calculates the sum of the digits in a positive integer N, where N can have up to 1000 digits.
"""

def sum_of_digits(N):
    """
    Calculate the sum of the digits in a positive integer N, 
    where N can have up to 1000 digits.

    Parameters:
    N (int): A positive integer with up to 1000 digits.

    Returns:
    int: The sum of the digits in N.
    """
    # Convert the integer to a string
    str_N = str(N)
    
    # Initialize the sum variable
    sum = 0
    
    # Iterate over each character in the string
    for char in str_N:
        # Convert the character back to an integer and add it to the sum
        sum += int(char)
    
    # Return the sum of the digits
    return sum