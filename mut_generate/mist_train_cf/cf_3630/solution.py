"""
QUESTION:
Write a function named `sum_of_primes` that calculates the sum of prime numbers within a given array that are greater than 10 and less than 20. If no prime numbers in the array satisfy this condition, return -1.
"""

def sum_of_primes(nums):
    """
    This function calculates the sum of prime numbers within a given array that are greater than 10 and less than 20.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    int: The sum of prime numbers greater than 10 and less than 20 in the array. Returns -1 if no prime numbers satisfy the condition.
    """
    
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n**0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    prime_sum = sum(num for num in nums if 10 < num < 20 and is_prime(num))
    
    return prime_sum if prime_sum != 0 else -1