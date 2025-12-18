"""
QUESTION:
Write a function named `square_area` that calculates the area of a square with each side equal to the sum of the first n prime numbers, where n is a given positive integer. The function should take an integer n as input and return the calculated area.
"""

def square_area(n):
    """
    Calculate the area of a square with each side equal to the sum of the first n prime numbers.
    
    Args:
    n (int): A positive integer representing the number of prime numbers to sum.
    
    Returns:
    int: The calculated area of the square.
    """
    
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Find the sum of the first n prime numbers
    prime_sum = 0
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            prime_sum += num
            count += 1
        num += 1

    # Calculate the area of the square
    area = prime_sum ** 2
    return area