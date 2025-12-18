"""
QUESTION:
Create a function named `is_prime` that takes an integer `n` as input and returns a boolean value indicating whether `n` is a prime number. The function should consider that prime numbers are integers greater than 1 with only two factors: 1 and the number itself.
"""

def is_prime(n):
    """
    Check if a number is a prime number

    Parameters:
    n (int): input number

    Returns:
    bool: True if the number is prime, False otherwise
    """
    
    # Check the input: if n is less than 2, it is not a prime number
    if n < 2:
        return False
    
    # Check the factors from 2 to sqrt(n) + 1
    for i in range(2, int(n**0.5) + 1):
        # If n has any factor in this range, it is not a prime number
        if n % i == 0:
            return False

    # If no factors found, n is a prime number
    return True