"""
QUESTION:
Write a function `find_prime_sum` that takes two integers `min_num` and `max_num` as input, finds all prime numbers in the range from `min_num` to `max_num` (inclusive), and returns the sum of these prime numbers. The function should not include `min_num` if it's not a prime number and should include `max_num` if it is a prime number.
"""

def find_prime_sum(min_num, max_num):
    """
    This function calculates the sum of all prime numbers within a given range.
    
    Args:
        min_num (int): The minimum number in the range (inclusive).
        max_num (int): The maximum number in the range (inclusive).
    
    Returns:
        int: The sum of all prime numbers in the given range.
    """
    
    def is_prime(n):
        """Helper function to check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Initialize sum of primes
    prime_sum = 0
    
    # Iterate over the range from min_num to max_num
    for num in range(min_num, max_num + 1):
        # Check if the number is prime
        if is_prime(num):
            # Add the prime number to the sum
            prime_sum += num
    
    return prime_sum