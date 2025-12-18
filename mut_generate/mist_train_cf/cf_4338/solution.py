"""
QUESTION:
Implement a function `check_prime` that checks whether a given integer is a prime number within the range of 10,000 to 20,000 and is divisible by both 3 and 5. The function should have a time complexity of O(n^(1/2)) and a space complexity of O(1).
"""

import math

def check_prime(n):
    """
    Checks whether a given integer is a prime number within the range of 10,000 to 20,000 and is divisible by both 3 and 5.
    
    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number is a prime number within the range of 10,000 to 20,000 and is divisible by both 3 and 5, False otherwise.
    """
    # Check if the number is within the range of 10,000 to 20,000
    if not 10000 <= n <= 20000:
        return False

    # Check if the number is divisible by both 3 and 5
    if n % 3 != 0 or n % 5 != 0:
        return False

    # Check if the number is a prime number
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True