"""
QUESTION:
Create a function `filter_primes` that takes a list of integers as input and returns a new list containing only the prime numbers. The function should handle negative integers by treating them as their positive counterparts when determining primality. The input list will only contain integers and will have a length of less than or equal to 1000. You cannot use any built-in functions or libraries to check for primality, and you must implement your own algorithm to determine the primality of each number.
"""

def filter_primes(lst):
    def is_prime(num):
        """
        Checks if a number is prime.
        
        Args:
        num (int): The number to check.
        
        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [x for x in lst if is_prime(abs(x))]