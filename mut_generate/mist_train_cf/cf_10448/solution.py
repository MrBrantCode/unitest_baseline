"""
QUESTION:
Write a function `sum_odd_at_prime_index` that calculates the sum of all odd values in a given 2D list `data` where the column index is a prime number. The function should return the calculated sum. The column index is considered prime if its 1-based index (i.e., index + 1) is a prime number.
"""

def is_prime(num):
    """
    Helper function to check if a number is prime.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def sum_odd_at_prime_index(data):
    """
    Calculates the sum of all odd values in a given 2D list where the column index is a prime number.
    
    Args:
    data (list): A 2D list of integers.
    
    Returns:
    int: The calculated sum.
    """
    total_sum = 0
    for row in data:
        for index, value in enumerate(row):
            # Check if the value is odd and its 1-based index is prime
            if value % 2 != 0 and is_prime(index + 1):
                total_sum += value
    return total_sum