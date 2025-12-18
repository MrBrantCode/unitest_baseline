"""
QUESTION:
Create a function `is_prime_palindrome(num)` that checks if a given integer `num` is a prime palindrome number. A prime palindrome number is a number that is both prime (only divisible by 1 and itself) and a palindrome (reads the same backward as forward). The function should return `True` if `num` is a prime palindrome and `False` otherwise.
"""

def is_prime_palindrome(num):
    """
    Checks if a given integer is a prime palindrome number.
    
    A prime palindrome number is a number that is both prime (only divisible by 1 and itself)
    and a palindrome (reads the same backward as forward).

    Args:
    num (int): The number to check.

    Returns:
    bool: True if num is a prime palindrome, False otherwise.
    """
    # Helper function to check if a number is prime
    def is_prime(n):
        # Check if the number is less than 2
        if n < 2:
            return False
        
        # Check if the number is divisible by any number from 2 to the square root of the number
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        
        return True

    # Helper function to check if a number is a palindrome
    def is_palindrome(n):
        # Convert the number to a string
        num_str = str(n)
        
        # Check if the string is equal to its reverse
        if num_str == num_str[::-1]:
            return True
        
        return False

    # Check if the number is both prime and a palindrome
    if is_prime(num) and is_palindrome(num):
        return True
    
    return False