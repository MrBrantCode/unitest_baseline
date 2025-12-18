"""
QUESTION:
Implement a function named `check_palindrome` that takes an integer `n` as input. This function should return a tuple of two boolean values indicating whether the number is a palindrome in decimal and binary representations, respectively.
"""

def check_palindrome(n):
    """
    This function checks whether a given integer is a palindrome in both decimal and binary representations.
    
    Args:
        n (int): The input number to be checked.
    
    Returns:
        tuple: A tuple containing two boolean values. The first value indicates whether the number is a palindrome in decimal representation,
               and the second value indicates whether the number is a palindrome in binary representation.
    """
    # Convert number to string
    str_n = str(n)
    # Check if the number is a palindrome in decimal representation
    decimal_palindrome = str_n == str_n[::-1]
    # Convert number to binary representation
    binary_n = bin(n).replace("0b", "")
    # Check if the number is a palindrome in binary representation
    binary_palindrome = binary_n == binary_n[::-1]
    # Return the results
    return decimal_palindrome, binary_palindrome